import pytest
from gilded_rose_completo import GildedRose, Item

def test_itens_normais():
    #arrange

    itens = [
        Item("Espada normal", validade = 10, qualidade= 20),
        Item("Espada vencida", validade = -1, qualidade= 30),
        Item("Espada sem qualidade", validade = 5, qualidade = 0)
    ]
    rose = GildedRose(itens)

    #act

    rose.atualizar_qualidade()

    #assert

    assert itens[0].validade == 9
    assert itens[0].qualidade == 19

    #garante que após a validade expirar a qualidade diminui 2x
    assert itens[1].validade == -2
    assert itens[1].qualidade == 28

    #garante que que a qualidade não fique negativa
    assert itens[2].validade == 4
    assert itens[2].qualidade == 0

def test_itens_aged_brie():
    #arrange 

    itens = [
        Item("Aged Brie", validade=2, qualidade=0),
        Item("Aged Brie", validade=-1, qualidade=10)
    ]

    rose = GildedRose(itens)

    #act

    rose.atualizar_qualidade()

    #assert

    assert itens[0].validade == 1
    assert itens[0].qualidade == 1

    assert itens[1].validade == -2
    assert itens[1].qualidade == 12

def test_itens_sulfuras():
    #arrange 
    itens = [
        Item("Sulfuras", validade=9, qualidade=80),
        Item("Sulfuras vencido", validade=-1, qualidade=80)
    ]
    rose = GildedRose(itens)

    #act
    rose.atualizar_qualidade()

    #assert
    assert itens[0].validade == 9 
    assert itens[0].qualidade == 80

    #ao executar o código, sulfuras vencidas tem o comportamento de um item qualquer vencido.
    assert itens[1].validade == -2
    assert itens[1].qualidade == 78

def test_itens_backstage_passes():
    #arrange
    itens = [
        Item("Backstage passes", validade=15, qualidade=20),
        Item("Backstage passes", validade=10, qualidade=49),
        Item("Backstage passes", validade=5, qualidade=49),
        Item("Backstage passes", validade=5, qualidade=19),
        Item("Backstage passes", validade=0, qualidade=19)
    ]
    rose = GildedRose(itens)

    #act
    rose.atualizar_qualidade()

    #assert 
    assert itens[0].validade == 14
    assert itens[0].qualidade == 21

    assert itens[1].validade == 9
    assert itens[1].qualidade == 50

    assert itens[2].validade == 4
    assert itens[2].qualidade == 50

    assert itens[3].validade == 4
    assert itens[3].qualidade == 22

    assert itens[4].validade == -1
    assert itens[4].qualidade == 0
    
