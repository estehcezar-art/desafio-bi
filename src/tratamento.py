import pandas as pd


def tratar_associados(associados):
    """
    Realiza o tratamento da base de associados.
    """

    associados = associados.copy()

    associados = associados.drop_duplicates()

    mapa_cidades = {
        "P. Branco": "Pato Branco",
        "PATO BRANCO": "Pato Branco",
        "Chapeco": "Chapecó",
        "Maringa": "Maringá"
    }

    associados["CIDADE"] = associados["CIDADE"].replace(mapa_cidades)

    mediana_agencia = associados.groupby( "AGENCIA")["RENDA_MENSAL"].transform("median")

    associados["RENDA_MENSAL"] = (associados["RENDA_MENSAL"].fillna(mediana_agencia))

    return associados

def tratar_produtos(produtos):
    """
    Realiza o tratamento da base de produtos.
    """

    produtos = produtos.copy()

    produtos = produtos.drop_duplicates()

    colunas_produtos = [
        "CONTA_CORRENTE",
        "CARTAO",
        "CREDITO",
        "INVESTIMENTO",
        "CONSORCIO",
        "SEGURO"
    ]

    for coluna in colunas_produtos:
        produtos[coluna] = (produtos[coluna].astype(str).str.strip().str.upper())

    return produtos

def tratar_movimentacao(movimentacao):
    """
    Realiza o tratamento da base de movimentação.
    """
    
    movimentacao = movimentacao.copy()

    movimentacao = movimentacao.drop_duplicates()

    return movimentacao