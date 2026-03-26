"""
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
"""

import os
import pandas as pd


def transform():
    print("🔄 Iniciando transformação...")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "data", "raw_data", "vagas.csv")

    print(f"📥 Lendo arquivo de: {file_path}")

    df = pd.read_csv(file_path)

    # Exemplo de transformação
    df["titulo"] = df["titulo"].str.upper()

    output_path = os.path.join(BASE_DIR, "data", "processed")
    os.makedirs(output_path, exist_ok=True)

    output_file = os.path.join(output_path, "vagas_tratadas.csv")

    df.to_csv(output_file, index=False)

    print("✅ Transformação concluída!")

if __name__ == "__main__":
        transform()