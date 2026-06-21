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

    #teste garante que após a validade expirar a qualidade diminui 2x
    assert itens[1].validade == -2
    assert itens[1].qualidade == 28

    #teste garante que que a qualidade não fique negativa
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