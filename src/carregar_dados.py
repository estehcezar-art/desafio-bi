import pandas as pd


def carregar_dados():
    arquivo = "data/raw/teste_bi_base_crua.xlsx"

    print("Carregando bases...")

    associados = pd.read_excel(
        arquivo,
        sheet_name="Associados"
    )

    produtos = pd.read_excel(
        arquivo,
        sheet_name="Produtos"
    )

    movimentacao = pd.read_excel(
        arquivo,
        sheet_name="Movimentacao"
    )

    print("Bases carregadas com sucesso!")

    return associados, produtos, movimentacao