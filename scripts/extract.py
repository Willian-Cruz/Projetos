""" 
import pandas as pd

def extract():
    dados = [{"titulo":"Analista de Dados", "empresa":"Empresa A", "localidade":"São Paulo","salario":5000},
             {"titulo":"Engenheiro de Dados", "empresa":"Empresa B", "localidade":"Rio de Janeiro","salario":8000},
             {"titulo":"Cientista de Dados", "empresa":"Empresa C", "localidade": None,"salario":9000},
            ]
    df = pd.DataFrame(dados)

    df.to_csv("../data/raw_data/vagas.csv", index=False)
    print("Dados extraídos com sucesso!")

if __name__ == "__main__":
    extract()
"""
import os
import pandas as pd


def extract():
    print("🚀 Iniciando etapa de extração...")

    # Simulação de dados (substitua pela sua raspagem depois)
    data = {
        "titulo": ["Analista de Dados", "Engenheiro de Dados"],
        "empresa": ["Empresa A", "Empresa B"],
        "localizacao": ["São Paulo", "Remoto"]
    }

    df = pd.DataFrame(data)

    # Caminho absoluto (baseado no projeto)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(BASE_DIR, "data", "raw_data")

    # Garante que a pasta existe
    os.makedirs(data_path, exist_ok=True)

    # Caminho final do arquivo
    file_path = os.path.join(data_path, "vagas.csv")

    print(f"📁 Salvando arquivo em: {file_path}")

    # Salva o CSV
    df.to_csv(file_path, index=False)

    print("✅ Extração concluída com sucesso!")


if __name__ == "__main__":
    extract()