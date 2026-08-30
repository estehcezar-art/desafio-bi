# Desafio de BI - Análise de Associados

Projeto desenvolvido como parte de um desafio técnico de BI com o objetivo de realizar o tratamento, consolidação e análise de dados de associados, produtos e movimentações financeiras.

O processamento dos dados foi desenvolvido em Python e a base resultante será utilizada para construção de um dashboard no Power BI.

## Objetivo

O projeto tem como objetivo transformar as bases disponibilizadas em informações que permitam analisar o perfil e o nível de relacionamento dos associados.

As principais etapas desenvolvidas são:

- análise e validação das bases de origem;
- tratamento e padronização dos dados;
- criação de indicadores;
- consolidação das bases através da chave do associado;
- criação de uma metodologia de classificação dos associados;
- geração de uma base processada para utilização no Power BI.

## Tecnologias utilizadas

- Python
- Pandas
- OpenPyXL
- Git
- GitHub
- Visual Studio Code
- Power BI

## Estrutura do projeto

```text
desafio-bi/
│
├── data/
│   ├── raw/
│   │   └── teste_bi_base_crua.xlsx
│   │
│   └── processed/
│       └── teste_bi_classificada.xlsx
│
├── src/
│   ├── main.py
│   ├── carregar_dados.py
│   ├── tratamento.py
│   ├── indicadores.py
│   ├── consolidacao.py
│   ├── classificacao.py
│   └── exportacao.py
│
├── .gitignore
└── README.md
```

## Bases utilizadas

O arquivo de origem possui três bases:

### Associados

Contém informações cadastrais dos associados:

- CHAVE
- NOME
- AGENCIA
- CIDADE
- DATA_ASSOCIACAO
- RENDA_MENSAL

### Produtos

Contém os produtos utilizados por cada associado:

- CONTA_CORRENTE
- CARTAO
- CREDITO
- INVESTIMENTO
- CONSORCIO
- SEGURO

### Movimentação

Contém informações relacionadas à movimentação financeira:

- SALDO_MEDIO
- PIX_MENSAL
- COMPRAS_CARTAO

As três bases são relacionadas através da coluna `CHAVE`.

## Tratamento dos dados

Durante a análise inicial foram realizadas verificações de:

- valores nulos;
- registros duplicados;
- chaves duplicadas;
- chaves nulas;
- padronização de cidades;
- consistência das datas;
- consistência dos valores numéricos.

### Renda mensal

Foram identificados valores nulos em `RENDA_MENSAL`.

Para o tratamento, os valores ausentes foram preenchidos utilizando a mediana de renda da respectiva agência.

A mediana foi escolhida por ser menos sensível a valores extremos do que a média e por preservar melhor o comportamento central da renda dos associados de cada agência.

### Cidades

Foram encontradas diferentes representações para algumas cidades, como:

- Pato Branco
- PATO BRANCO
- P. Branco

Esses valores foram padronizados para uma única nomenclatura.

Também foram ajustados nomes de cidades que necessitavam de acentuação.

### Datas futuras

Foram identificadas datas de associação posteriores à data atual.

Esses registros foram preservados na base original, porém o tempo de relacionamento não é calculado para essas ocorrências, evitando a geração de tempos negativos.

### Produtos

Os campos de produtos foram validados para garantir a consistência dos valores utilizados na identificação de posse de produtos.

### Movimentação

Foram analisados:

- saldo médio;
- quantidade mensal de PIX;
- compras no cartão.

Não foram identificados valores negativos.

Valores iguais a zero em `PIX_MENSAL` foram considerados válidos, representando associados que não realizaram transações PIX no período.

## Indicadores criados

### Quantidade de produtos

Foi criado o indicador:

`QTD_PRODUTOS`

Ele representa a quantidade total de produtos utilizados por cada associado.

### Faixa de renda

Os associados foram classificados nas seguintes faixas:

- Até R$ 3.000
- R$ 3.001 a R$ 8.000
- R$ 8.001 a R$ 15.000
- Acima de R$ 15.000

### Tempo de relacionamento

O tempo de relacionamento é calculado a partir da diferença entre a data atual e a data de associação.

Foram criados dois campos:

`TEMPO_RELACIONAMENTO_MESES`

Utilizado para cálculos e regras de classificação.

`TEMPO_RELACIONAMENTO`

Utilizado para apresentação, em formato mais amigável, por exemplo:

```text
2 anos e 9 meses
6 anos e 1 mês
5 anos
```

## Consolidação das bases

As bases de Associados, Produtos e Movimentação foram consolidadas utilizando a coluna `CHAVE`.

A base de associados foi utilizada como referência principal e as demais informações foram incorporadas através de relacionamentos do tipo `left join`.

Após a consolidação, a base permaneceu com 1.000 associados.

## Classificação dos associados

Foi desenvolvida uma metodologia de pontuação para classificar os associados de acordo com seu nível de relacionamento e utilização dos serviços.

Foram considerados os seguintes critérios:

| Critério | Pontuação máxima |
|---|---:|
| Quantidade de produtos | 2 |
| Tempo de relacionamento | 2 |
| Saldo médio | 1 |
| Utilização de PIX | 1 |
| Compras no cartão | 1 |
| **Total** | **7** |

### Quantidade de produtos

- 2 ou mais produtos: +1 ponto
- 4 ou mais produtos: +1 ponto adicional

### Tempo de relacionamento

- 2 anos ou mais: +1 ponto
- 4 anos ou mais: +1 ponto adicional

O cálculo é realizado utilizando o tempo de relacionamento em meses.

### Movimentação financeira

São atribuídos pontos adicionais quando o associado apresenta:

- saldo médio igual ou superior à mediana da base;
- quantidade mensal de PIX igual ou superior à mediana da base;
- compras no cartão iguais ou superiores à mediana da base.

A utilização da mediana permite que os critérios sejam definidos de acordo com a distribuição dos próprios dados.

## Regra de classificação

A pontuação final varia entre 0 e 7 pontos.

| Score | Classificação |
|---|---|
| 0 a 2 | Inicial |
| 3 a 4 | Em Desenvolvimento |
| 5 a 6 | Maduro |
| 7 | Engajado |

A metodologia foi definida buscando manter regras simples, transparentes e reproduzíveis, considerando quantidade de produtos, tempo de relacionamento e intensidade de utilização dos serviços.

## Resultado da classificação

Na execução atual da base foram obtidos:

| Classificação | Associados |
|---|---:|
| Inicial | 146 |
| Em Desenvolvimento | 483 |
| Maduro | 359 |
| Engajado | 12 |
| **Total** | **1.000** |

## Base processada

Ao final do processamento é gerado automaticamente o arquivo:

```text
data/processed/teste_bi_classificada.xlsx
```

Essa base contém os dados tratados, indicadores, score e classificação dos associados e será utilizada como fonte para o dashboard desenvolvido no Power BI.

## Execução do projeto

Com o ambiente virtual ativo, execute na raiz do projeto:

```bash
python src/main.py
```

O processo realiza:

```text
Carregamento
    ↓
Validação
    ↓
Tratamento
    ↓
Criação de indicadores
    ↓
Consolidação
    ↓
Classificação
    ↓
Exportação
```

## Dashboard

O dashboard será desenvolvido no Power BI utilizando a base processada gerada pelo pipeline Python.

Entre as análises previstas estão:

- distribuição dos associados por classificação;
- quantidade de associados por agência;
- quantidade de associados por cidade;
- distribuição por faixa de renda;
- utilização de produtos;
- saldo médio;
- utilização de PIX;
- compras no cartão;
- perfil dos associados por nível de relacionamento.

## Autor

**Estéfanos Cezar**