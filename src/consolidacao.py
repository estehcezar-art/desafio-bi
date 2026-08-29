def consolidar_bases(
    associados,
    produtos,
    movimentacao
):
    """
    Consolida as bases de associados, produtos e movimentação
    utilizando a coluna CHAVE.
    """

    base_consolidada = associados.merge(
        produtos,
        on="CHAVE",
        how="left"
    )

    base_consolidada = base_consolidada.merge(
        movimentacao,
        on="CHAVE",
        how="left"
    )

    return base_consolidada