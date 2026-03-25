import pandas as pd

def transform():
    df = pd.read_csv("../data/raw_data/vagas.csv")

    # Remover duplicados
    df = df.drop_duplicates()
    # Tratar valores nulos
    df["localidade"] = df["localidade"].fillna("Não indentificado")
    # Cria uma nova coluna
    df["nivel"] = df["titulo"].apply(
        lambda x: "Júnior" if "Analista" in x else "Sênior"
    )

    df.to_csv("../data/raw_data/processed/vagas_tratadas.csv", index=False)

    print("A transformação dos dados foi concluída com sucesso!")


if __name__ == "__main__":
        transform()