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