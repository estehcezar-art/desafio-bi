import pandas as pd

def criar_indicadores_produtos(produtos):
    produtos = produtos.copy()

    colunas_produtos = [
        "CONTA_CORRENTE",
        "CARTAO",
        "CREDITO",
        "INVESTIMENTO",
        "CONSORCIO",
        "SEGURO"
    ]

    produtos["QTD_PRODUTOS"] = (produtos[colunas_produtos] .eq("S").sum(axis=1))

    return produtos

def criar_indicadores_associados(associados):
    associados = associados.copy()

    hoje = pd.Timestamp.today().normalize()

    associados["TEMPO_RELACIONAMENTO_ANOS"] = ((hoje - associados["DATA_ASSOCIACAO"]).dt.days / 365.25)

    associados.loc[associados["DATA_ASSOCIACAO"] > hoje, "TEMPO_RELACIONAMENTO_ANOS"] = pd.NA

    associados["TEMPO_RELACIONAMENTO_ANOS"] = (associados["TEMPO_RELACIONAMENTO_ANOS"].round(2))

    associados["FAIXA_RENDA"] = pd.cut(
        associados["RENDA_MENSAL"],
        bins=[
            float("-inf"),
            3000,
            8000,
            15000,
            float("inf")
        ],
        labels=[
            "Até R$ 3.000",
            "R$ 3.001 a R$ 8.000",
            "R$ 8.001 a R$ 15.000",
            "Acima de R$ 15.000"
        ]
    )

    return associados