"""
Projeto Final - Gilded Rose Refactoring Kata (versão completa)

Você é responsável pela manutenção do sistema de uma loja chamada
"Gilded Rose". A loja vende todo tipo de itens, e o sistema precisa
atualizar a qualidade e validade dos itens diariamente.

O dono da loja, Allison, escreveu uma especificação (em REGRAS_DE_NEGOCIO.md)
e um código que funciona, mas é difícil de manter. Allison quer adicionar
um novo tipo de item ("Conjurado"), mas tem medo de quebrar tudo.

Sua missão completa está em INSTRUCOES_PROJETO_FINAL.md.

NÃO modifique a classe Item nem suas propriedades, Allison não tem
permissão (a classe é da empresa Goblin que fornece o pacote).
"""


class Item:
    def __init__(self, nome: str, validade: int, qualidade: int):
        self.nome = nome
        self.validade = validade
        self.qualidade = qualidade

    def __repr__(self):
        return f"{self.nome}, {self.validade}, {self.qualidade}"


class GildedRose:
    def __init__(self, itens: list[Item]):
        self.itens = itens

    def atualizar_aged_brie(self, item):

        item.validade -= 1

        if item.validade >= 0:
            item.qualidade += 1 

        elif item.validade < 0:
            item.qualidade += 2

        if item.qualidade > 50:
            item.qualidade = 50

        if item.qualidade < 0:
            item.qualidade = 0


    def atualizar_sulfuras(self, item):
        item.qualidade = 80


    def atualizar_backstage_passes(self, item):
        if item.validade >= 11:
            item.qualidade += 1

        elif item.validade >= 6:
            item.qualidade += 2

        elif item.validade > 0:
            item.qualidade += 3

        item.validade -= 1

        if item.validade < 0:
            item.qualidade = 0

        if item.qualidade > 50:
            item.qualidade = 50


    def atualizar_itens_normais(self, item):
        if item.validade >= 0:
            item.qualidade -= 1

        elif item.validade < 0:
            item.qualidade -= 2
        item.validade -= 1

        if item.qualidade < 0:
            item.qualidade = 0

    def atualizar_conjurado(self, item):
        if item.validade >= 0:
            item.qualidade -= 2

        elif item.validade < 0:
            item.qualidade -= 4
        item.validade -= 1

        if item.qualidade < 0:
            item.qualidade = 0 

    def atualizar_qualidade(self):
        for item in self.itens:

            if (item.nome == "Aged Brie"):
                self.atualizar_aged_brie(item)

            elif (item.nome == "Sulfuras"):
                self.atualizar_sulfuras(item)

            elif (item.nome == "Backstage passes"):
                self.atualizar_backstage_passes(item)

            elif (item.nome == "Conjurado"):
                self.atualizar_conjurado(item)

            else:
                self.atualizar_itens_normais(item)


if __name__ == "__main__":
    itens = [
        Item("Espada normal", validade=10, qualidade=20),
        Item("Aged Brie", validade=2, qualidade=0),
        Item("Espada vencida", validade=0, qualidade=7),
        Item("Sulfuras", validade=0, qualidade=80),
        Item("Sulfuras vencido", validade=-1, qualidade=80),
        Item("Backstage passes", validade=15, qualidade=20),
        Item("Backstage passes", validade=10, qualidade=49),
        Item("Backstage passes", validade=5, qualidade=49),
        Item("Conjurado", validade=10, qualidade=20),
        Item("Conjurado", validade=-1, qualidade=2)
    ]
    rose = GildedRose(itens)
    print("Dia 0:")
    for item in rose.itens:
        print(f"  {item}")
    rose.atualizar_qualidade()
    print("\nDia 1:")
    for item in rose.itens:
        print(f"  {item}")
