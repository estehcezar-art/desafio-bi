def identificar_oportunidades(base):
    """
    Identifica oportunidades comerciais na base de associados.
    """

    base = base.copy()

    base["OPORT_ALTA_RENDA_POUCOS_PRODUTOS"] = (
        (base["RENDA_MENSAL"] > 15000)
        & (base["QTD_PRODUTOS"] <= 2)
    )

    mediana_pix = base["PIX_MENSAL"].median()
    mediana_cartao = base["COMPRAS_CARTAO"].median()

    base["OPORT_BAIXA_UTILIZACAO"] = (
        (base["PIX_MENSAL"] < mediana_pix)
        & (base["COMPRAS_CARTAO"] < mediana_cartao)
    )

    mediana_renda = base["RENDA_MENSAL"].median()
    mediana_saldo = base["SALDO_MEDIO"].median()

    base["OPORT_POTENCIAL_CRESCIMENTO"] = (
    base["CLASSIFICACAO"].isin([
        "Inicial",
        "Em Desenvolvimento"
    ])
    & (
        (base["RENDA_MENSAL"] > mediana_renda)
        | (base["SALDO_MEDIO"] > mediana_saldo)
    ))

    base["QTD_OPORTUNIDADES"] = (
    base["OPORT_ALTA_RENDA_POUCOS_PRODUTOS"].astype(int)
    + base["OPORT_BAIXA_UTILIZACAO"].astype(int)
    + base["OPORT_POTENCIAL_CRESCIMENTO"].astype(int)
    )

    return base