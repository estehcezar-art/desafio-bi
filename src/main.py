import pandas as pd
from carregar_dados import carregar_dados


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
    associados, produtos, movimentacao = carregar_dados()

    analisar_base("ASSOCIADOS", associados)
    analisar_base("PRODUTOS", produtos)
    analisar_base("MOVIMENTACAO", movimentacao)

    print("\n--- ASSOCIADOS COM RENDA NÃO INFORMADA ---")

    renda_nula = associados[
        associados["RENDA_MENSAL"].isnull()
    ]

    print(renda_nula)

    print("\n--- ESTATÍSTICAS DE RENDA ---")
    print(associados["RENDA_MENSAL"].describe())

    print("\n--- MEDIANA DE RENDA POR AGÊNCIA ---")
    print(
        associados.groupby("AGENCIA")["RENDA_MENSAL"]
        .median()
    )

    print("\n--- QUANTIDADE DE ASSOCIADOS POR AGÊNCIA ---")
    print(
        associados["AGENCIA"]
        .value_counts()
        .sort_index()
    )

    print("\n--- CIDADES CADASTRADAS ---")
    print(
        sorted(associados["CIDADE"].unique())
    )

    print("\n--- DATAS DE ASSOCIAÇÃO FUTURAS ---")

    hoje = pd.Timestamp.today().normalize()

    datas_futuras = associados[
        associados["DATA_ASSOCIACAO"] > hoje
    ]

    print(datas_futuras)

    print(
        f"\nQuantidade de datas futuras: {len(datas_futuras)}"
    )


if __name__ == "__main__":
    main()