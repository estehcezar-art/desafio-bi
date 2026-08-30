from pathlib import Path


def exportar_base(base):
    """
    Exporta a base processada para um arquivo Excel.
    """

    pasta_saida = Path("data/processed")

    pasta_saida.mkdir(
        parents=True,
        exist_ok=True
    )

    arquivo_saida = pasta_saida / "teste_bi_classificada.xlsx"

    base.to_excel(
        arquivo_saida,
        index=False
    )

    print(
        f"\nBase exportada com sucesso para: "
        f"{arquivo_saida}"
    )