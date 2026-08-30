def classificar_associados(base):
    """
    Classifica os associados com base em relacionamento,
    quantidade de produtos e movimentação financeira.
    """

    base = base.copy()

    base["SCORE"] = 0

    base.loc[
        base["QTD_PRODUTOS"] >= 2,
        "SCORE"
    ] += 1

    base.loc[
        base["QTD_PRODUTOS"] >= 4,
        "SCORE"
    ] += 1

    base.loc[
        base["TEMPO_RELACIONAMENTO_MESES"] >= 24,
        "SCORE"
    ] += 1

    base.loc[
        base["TEMPO_RELACIONAMENTO_MESES"] >= 48,
        "SCORE"
    ] += 1

    mediana_saldo = base["SALDO_MEDIO"].median()

    base.loc[
        base["SALDO_MEDIO"] >= mediana_saldo,
        "SCORE"
    ] += 1

    mediana_pix = base["PIX_MENSAL"].median()

    base.loc[
        base["PIX_MENSAL"] >= mediana_pix,
        "SCORE"
    ] += 1

    mediana_cartao = base["COMPRAS_CARTAO"].median()

    base.loc[
        base["COMPRAS_CARTAO"] >= mediana_cartao,
        "SCORE"
    ] += 1

    def definir_classificacao(score):
        if score <= 2:
            return "Inicial"
        elif score <= 4:
            return "Em Desenvolvimento"
        elif score <= 6:
            return "Maduro"
        else:
            return "Engajado"

    base["CLASSIFICACAO"] = base["SCORE"].apply( definir_classificacao)

    return base