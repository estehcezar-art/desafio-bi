import pandas as pd
from carregar_dados import carregar_dados
from tratamento import (tratar_associados,tratar_produtos,tratar_movimentacao)
from indicadores import criar_indicadores_produtos

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
    print("\n--- DATAS DE ASSOCIAÇÃO FUTURAS ---")

    hoje = pd.Timestamp.today().normalize()

    datas_futuras = associados[associados["DATA_ASSOCIACAO"] > hoje]

    print(datas_futuras)

    print( f"\nQuantidade de datas futuras: {len(datas_futuras)}")

    associados_tratados = tratar_associados(associados)

    print("\n" + "=" * 50)
    print("VALIDAÇÃO APÓS TRATAMENTO")
    print("=" * 50)

    print("\nValores nulos:")
    print(associados_tratados.isnull().sum())

    print("\nCidades:")
    print(sorted(associados_tratados["CIDADE"].unique()))

    print("\nRegistros duplicados:")
    print(associados_tratados.duplicated().sum())

    produtos_tratados = tratar_produtos(produtos)

    print("\n" + "=" * 50)
    print("VALIDAÇÃO DA BASE DE PRODUTOS")
    print("=" * 50)

    colunas_produtos = [
    "CONTA_CORRENTE",
    "CARTAO",
    "CREDITO",
    "INVESTIMENTO",
    "CONSORCIO",
    "SEGURO"
    ]

    for coluna in colunas_produtos:
        print(f"\n{coluna}:")
        print(produtos_tratados[coluna].value_counts(dropna=False))

    produtos_indicadores = criar_indicadores_produtos(produtos_tratados)

    print("\n" + "=" * 50)
    print("INDICADORES DE PRODUTOS")
    print("=" * 50)

    print(produtos_indicadores[["CHAVE", "QTD_PRODUTOS"]].head(10))

    print("\nDistribuição da quantidade de produtos:")
    print(produtos_indicadores["QTD_PRODUTOS"].value_counts().sort_index())

    movimentacao_tratada = tratar_movimentacao(movimentacao)

    print("\n" + "=" * 50)
    print("VALIDAÇÃO DA BASE DE MOVIMENTAÇÃO")
    print("=" * 50)

    colunas_movimentacao = [
    "SALDO_MEDIO",
    "PIX_MENSAL",
    "COMPRAS_CARTAO"
    ]

    for coluna in colunas_movimentacao:
        print(f"\n--- {coluna} ---")

        print("Estatísticas:")
        print(movimentacao_tratada[coluna].describe())

        print(f"Valores negativos: "
              f"{(movimentacao_tratada[coluna] < 0).sum()}")

        print(f"Valores iguais a zero: "
              f"{(movimentacao_tratada[coluna] == 0).sum()}")

if __name__ == "__main__":
    main()