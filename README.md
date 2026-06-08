# Projeto Final - Gilded Rose

Bem-vindo ao repositório-base do **Projeto Final** do curso de Boas Práticas para o Desenvolvimento de Software.

Este repositório contém um sistema de inventário de uma loja chamada **Gilded Rose**. O sistema funciona, mas o código está difícil de manter, e o seu trabalho é refatorá-lo com segurança e adicionar uma funcionalidade nova, aplicando tudo que você aprendeu no curso.

## O que tem aqui

| Arquivo | O que é |
|---------|---------|
| `gilded_rose_completo.py` | O código do sistema que você vai refatorar |
| `REGRAS_DE_NEGOCIO.md` | A especificação do sistema (o que cada item deve fazer) |
| `INSTRUCOES_PROJETO_FINAL.md` | O enunciado do projeto: tarefa, passo a passo, cronograma e rubrica de avaliação |
| `README.md` | Este arquivo |

## Por onde começar

1. **Leia o `INSTRUCOES_PROJETO_FINAL.md`** - é o enunciado completo, com o passo a passo e como você será avaliado.
2. **Leia o `REGRAS_DE_NEGOCIO.md`** - entenda o que o sistema deve fazer antes de mexer no código.
3. **Faça o fork e comece** (o passo a passo está nas instruções).

## Como rodar o sistema

Requer Python 3.10 ou superior.

```bash
python gilded_rose_completo.py
```

Você verá o estado dos itens no "Dia 0" e no "Dia 1" após uma atualização. Observe o comportamento, é o que você vai documentar com testes antes de refatorar.

## Como rodar os testes

Depois de instalar as dependências e escrever seus testes:

```bash
pip install pytest pytest-cov
python -m pytest -v
```

## Resumo da missão

1. **Caracterizar** - escrever testes que documentam o comportamento atual (sua rede de segurança).
2. **Refatorar** - limpar o código mantendo os testes verdes.
3. **Adicionar a feature "Conjurado"** - o novo tipo de item pedido pela dona da loja.
4. **Documentar e entregar** - README, decisões, e abrir o Pull Request.

A regra de ouro: **não modifique a classe `Item`** (ela é de uma empresa parceira). E **comece pelos testes**, sem eles, refatorar é jogo de azar.

Os detalhes completos estão em `INSTRUCOES_PROJETO_FINAL.md`. Boa sorte!
