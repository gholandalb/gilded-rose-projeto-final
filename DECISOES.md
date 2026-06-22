# Mudanças Realizadas - Gilded Rose

Este arquivo contém as mudanças que foram feitas ao decorrer do projeto de refatoração, incluindo novas funções, refatorações e a criação de testes.

## Testes

### 1. Itens normais 
Foram realizados 3 testes, garantindo, respectivamente, que:

- Em casos ordinários o programa funciona corretamente.
- Quando a validade expirar a qualidade decairá em 2x.
- Garante que a qualidade não possa ficar negativa.

### 2. Itens Aged Brie 
Foram realizados 2 testes, garantindo, respectivamente, que:

- A qualidada aumenta 1 ponto caso esteja dentro da validade.
- A qualidade aumenta 2 pontos caso a validade seja menor que 0.

### 3. Itens Sulfuras
2 testes foram feitos para confirmar o comportamento do item sulfura normal e do item sulfura vencido. 

    OBS: foi notado que o item sulfura vencido tem o mesmo comportamento de um item normal vencido.

### 4. Itens Backstage passes 
Tipo de item com a maior quantidade de testes realizado para garantir que:
- A qualidade não passe de 50
- 11 ou mais dias antes: ganha 1 de qualidade por dia.
- 10 a 6 dias antes: ganha 2 de qualidade por dia.
- 5 a 0 dias antes: ganha 3 de qualidade por dia.
- Quando a validade for menor que 0 a qualidade vira 0. 

## Refatoração

Com partida na função *atualizar_qualidade()* foram criadas 4 funções para atualizar cada tipo de item independentemente. Sendo essas:
```python
    atualizar_aged_brie()
    atualizar_sulfuras()
    atualizar_backstage_passes()
    atualizar_itens_normais()
```
Além disso, a função *atualizar_qualidade()* tempo apenas o papel de chamar a função adequada dependendo do tipo do item.
