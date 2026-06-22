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

- a qualidada aumenta 1 ponto caso esteja dentro da validade.
- a qualidade aumenta 2 pontos caso a validade seja menor que 0.

### 3. Itens Sulfuras
2 testes foram feitos para confirmar o comportamento do item sulfura normal e do item sulfura vencido. 

    OBS: foi notado que o item sulfura vencido tem o mesmo comportamento de um item normal vencido.
