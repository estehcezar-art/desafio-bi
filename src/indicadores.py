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

    produtos["FAIXA_PRODUTOS"] = pd.cut(
        produtos["QTD_PRODUTOS"],
        bins=[
            -1,
            1,
            3,
            6
        ],
        labels=[
            "0 a 1 produto",
            "2 a 3 produtos",
            "4 a 6 produtos"
        ]
    )

    return produtos

def formatar_tempo_relacionamento(total_meses):
    if pd.isna(total_meses):
        return pd.NA

    anos = int(total_meses // 12)
    meses = int(total_meses % 12)

    partes = []

    if anos > 0:
        partes.append(f"{anos} {'ano' if anos == 1 else 'anos'}")

    if meses > 0:
        partes.append(f"{meses} {'mês' if meses == 1 else 'meses'}")

    if not partes:
        return "0 meses"

    return " e ".join(partes)

def criar_indicadores_associados(associados):
    associados = associados.copy()

    hoje = pd.Timestamp.today().normalize()

    datas = associados["DATA_ASSOCIACAO"]

    meses = ((hoje.year - datas.dt.year) * 12 
             + (hoje.month - datas.dt.month)
             - (hoje.day < datas.dt.day).astype(int))

    meses = meses.where(datas <= hoje, pd.NA)

    associados["TEMPO_RELACIONAMENTO_MESES"] = meses.astype("Int64")

    associados["TEMPO_RELACIONAMENTO"] = (
        associados["TEMPO_RELACIONAMENTO_MESES"]
        .apply(formatar_tempo_relacionamento))

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

    associados["FAIXA_TEMPO_RELACIONAMENTO"] = pd.cut(
        associados["TEMPO_RELACIONAMENTO_MESES"],
        bins=[
            float("-inf"),
            24, 
            60,
            96,
            float("inf")
        ],
        labels=[
            "Até 2 anos",
            "De 2 a 5 anos",
            "De 5 a 8 anos",
            "Acima de 8 anos"
        ]
    )
    
    return associados