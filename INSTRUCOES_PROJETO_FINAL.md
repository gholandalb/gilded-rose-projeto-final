# Projeto Final Integrador - Refatoração Gilded Rose

## Sobre

Este é o projeto final do curso. Vale **50% da nota total**. Aqui você vai aplicar **TUDO** que aprendeu no curso:

- Identificação de code smells (Módulo 1)
- Boas práticas de codificação (Módulo 2)
- Versionamento, branches e PRs (Módulo 3)
- Testes automatizados (Módulo 4)
- Documentação técnica (Módulo 4)
- Refatoração com segurança (Módulo 4)

## Cronograma

- **Apresentação (hoje):** apresentação do projeto e primeiras dúvidas. Você recebe os arquivos.
- **Período de desenvolvimento:** as próximas aulas reservam tempo para dúvidas e acompanhamento.
- **Entrega:** 48h antes da apresentação final, no GitHub.
- **Apresentação final:** defesa de 8 minutos por aluno.

> As datas exatas serão combinadas conforme o calendário da turma.

## Como começar (setup com fork)

O projeto vive num repositório no GitHub. Você vai trabalhar nele usando o fluxo profissional completo de contribuição, o mesmo do Módulo 3: **fork → clone → branch → commits → Pull Request.**

### Passo 1 — Fazer o fork

1. Acesse o repositório do projeto no GitHub (link no canal da turma).
2. Clique em **Fork** (canto superior direito). Isso cria uma **cópia na sua conta**.
3. Aguarde o GitHub criar seu fork, agora você tem `github.com/SEU_USUARIO/gilded-rose-projeto-final`.

> Fork é uma cópia do repositório na sua conta, onde você tem total liberdade pra trabalhar sem afetar o original.

### Passo 2 - Clonar o seu fork

```bash
git clone https://github.com/SEU_USUARIO/gilded-rose-projeto-final.git
cd gilded-rose-projeto-final
```

> Atenção: clone o **seu fork** (com seu usuário na URL), não o repositório original.

### Passo 3 - Criar sua branch de trabalho

```bash
git switch -c refatoracao
```

Trabalhe sempre nesta branch, não na `main`.

### Passo 4 - Trabalhar e commitar em passos pequenos

Conforme você avança (testes, refatoração, feature nova), faça commits pequenos em Conventional Commits:

```bash
git add .
git commit -m "test: adiciona testes de caracterizacao para itens normais"
# ... mais trabalho ...
git commit -m "refactor: extrai logica de Aged Brie para classe propria"
```

### Passo 5 - Enviar e abrir o Pull Request

```bash
git push -u origin refatoracao
```

Depois, no GitHub:
1. Vá ao seu fork, aparece a faixa **"Compare & pull request"**. Clique.
2. **Importante - confira o destino do PR:** ele deve ir da sua branch `refatoracao` (do seu fork) **de volta para o repositório ORIGINAL do curso** (base: `main` do repositório original). O GitHub mostra isso no topo: `repositório-original/main` ← `seu-fork/refatoracao`.
3. Escreva um título e uma descrição claros (o que mudou, por quê, como testar).
4. Clique em **Create pull request**.

> Você **não precisa mergear**, só abrir o PR.

---

## Sua missão

Você recebeu o sistema da loja Gilded Rose: um arquivo `gilded_rose_completo.py` com a classe `GildedRose` e o método `atualizar_qualidade`. As regras de negócio estão em `REGRAS_DE_NEGOCIO.md`.

Você deve, **nesta ordem**:

### 1. Caracterização - entender o sistema

- Ler `REGRAS_DE_NEGOCIO.md` com calma.
- Rodar o código atual e observar o comportamento.
- Escrever **testes de caracterização** (golden master) que documentem o comportamento atual pra cada tipo de item.

> Esta é exatamente a habilidade da Aula 10: escrever testes com estrutura AAA. Aqui você usa pra "fotografar" o que o código faz hoje, criando sua rede de segurança.

### 2. Refatoração principal

- Refatorar `atualizar_qualidade` mantendo os testes verdes.
- Aplicar nomes claros, funções pequenas, eliminar aninhamento.
- Considerar polimorfismo (cada tipo de item sabe se atualizar).
- Manter commits pequenos e em Conventional Commits.

### 3. Adicionar a feature "Conjurado"

- Após refatorado, adicione o novo tipo de item conforme as regras.
- Acrescentar testes para "Conjurado".
- Se sua refatoração estiver boa, adicionar o tipo NOVO deve ser fácil, sem mudar código existente. (Esse é o sinal de uma boa refatoração!)

### 4. Documentação

- Escrever um `README.md` completo.
- Adicionar docstrings nas funções/classes públicas.
- Documentar decisões importantes em `DECISOES.md`.

### 5. Polimento e entrega

- Medir cobertura (`pytest --cov`). Mirar 85%+.
- Revisar o histórico de commits.
- Confirmar que o Pull Request (do seu fork para o repositório original) está aberto e com descrição clara.
- Preparar a apresentação de 8 min.

## Restrições importantes

- **NÃO modifique a classe `Item`.** É de uma empresa parceira (Goblin). Adicionar propriedades quebra outros sistemas.
- Pode adicionar **novas classes**.
- Pode mudar o método **`atualizar_qualidade`** como quiser.
- Pode usar Python moderno (type hints, etc.).

## Estrutura esperada do repositório

Ao final, seu repositório (o fork) deve ter os arquivos que **vieram da base** mais os que **você criou**:

```
gilded-rose-projeto-final/   (seu fork)
├── README.md                      (veio na base - pode melhorar)
├── REGRAS_DE_NEGOCIO.md           (veio na base - mantenha)
├── INSTRUCOES_PROJETO_FINAL.md    (veio na base - mantenha)
├── gilded_rose.py                 (você refatora - pode renomear de gilded_rose_completo.py)
├── DECISOES.md                    (você cria - registra suas escolhas)
├── tests/                         (você cria)
│   ├── test_caracterizacao.py
│   ├── test_conjurado.py
│   └── ...
└── .gitignore                     (veio na base)
```

> Os arquivos que vieram na base **não somem**, eles continuam no seu fork. Você apenas **adiciona** os novos (testes, `DECISOES.md`) e refatora o código.

## Apresentação (8 min)

Estrutura sugerida:

| Seção | Tempo | Conteúdo |
|-------|-------|----------|
| Contexto | 1 min | O que é o sistema, qual era o problema |
| Diagnóstico | 2 min | Code smells identificados (com exemplos do código original) |
| Refatorações aplicadas | 3 min | 2-3 mudanças importantes (mostre o diff) |
| Testes adicionados | 1 min | Suíte de testes e cobertura final |
| Aprendizados | 1 min | Reflexão honesta, o que faria diferente |

## Critério de avaliação (rubrica)

| Critério | Peso | 0-2 | 3-4 | 5 |
|----------|------|-----|-----|---|
| Identificação de code smells | 15% | Não identificou | Identificou alguns | Identificou bem, com vocabulário técnico |
| Refatorações aplicadas | 25% | Mudou pouco | Refatorou alguns pontos | Refatorou com qualidade visível |
| Testes (cobertura e qualidade) | 20% | Ausente | Básico | Suíte consistente, >85% cobertura |
| Feature "Conjurado" funciona | 10% | Não implementou | Implementou com bug | Funciona conforme spec |
| Documentação (README, docstrings) | 15% | Ausente | Mínima | Completa e clara |
| Git (commits, branches, PR) | 10% | Bagunçado | Aceitável | Commits convencionais e organizados |
| Apresentação | 5% | Confusa | Ok | Clara e técnica |

**Total:** 100 pontos. Convertido pra 60% da nota total.

## Dicas finais

- **Comece pelos testes.** Sem testes, refatoração é jogo de azar.
- **Commits pequenos.** Cada mudança coerente é um commit. Evite commits gigantes.
- **Não tente fazer perfeito.** Faça progresso. Entrega > perfeição.
- **Se travar:** poste no canal da turma. A gente se ajuda.
- **Entrega 48h antes:** dá tempo de revisar e descansar antes da apresentação.

## Atenção: um detalhe que você vai descobrir

Ao escrever os testes de caracterização, você pode encontrar comportamentos que **parecem** contradizer as regras de negócio. Não "conserte" isso durante a caracterização — apenas **documente o que o código faz hoje**. Refatoração preserva comportamento. Se algo parece um bug, anote em `DECISOES.md` e discuta na apresentação. (Dica: preste atenção no Sulfuras vencido.)


Boa sorte!
