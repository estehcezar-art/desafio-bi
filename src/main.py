import pandas as pd


def analisar_base(nome, df):
    print(f"\n{'=' * 50}")
    print(f"ANÁLISE DA BASE: {nome}")
    print(f"{'=' * 50}")

    print(f"\nQuantidade de registros: {len(df)}")
    print(f"Quantidade de colunas: {len(df.columns)}")

    print("\n--- TIPOS DE DADOS ---")
    print(df.dtypes)

    print("\n--- VALORES NULOS ---")
    print(df.isnull().sum())

    print("\n--- REGISTROS DUPLICADOS ---")
    print(f"Duplicados: {df.duplicated().sum()}")

    print("\n--- CHAVES DUPLICADAS ---")
    print(f"CHAVEs duplicadas: {df['CHAVE'].duplicated().sum()}")

    print("\n--- CHAVES NULAS ---")
    print(f"CHAVEs nulas: {df['CHAVE'].isnull().sum()}")


def main():

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

    analisar_base("ASSOCIADOS", associados)
    analisar_base("PRODUTOS", produtos)
    analisar_base("MOVIMENTACAO", movimentacao)


if __name__ == "__main__":
    main()