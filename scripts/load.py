"""
import pandas as pd
import sqlite3

def load():
    conn = sqlite3.connect("../data/vagas.db")

    df = pd.read_csv("../data/raw_data/processed/vagas_tratadas.csv")

    df.to_sql("vagas", conn, if_exists="replace", index=False)

    conn.close()

    print("Dados carregados no banco!")
"""
import os
import pandas as pd


def load():
    print("📦 Iniciando carga...")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    file_path = os.path.join(BASE_DIR, "data", "processed", "vagas_tratadas.csv")

    print(f"📥 Lendo arquivo de: {file_path}")

    df = pd.read_csv(file_path)

    print("✅ Carga concluída!")
    print(df.head())


if __name__ == "__main__":
    load()