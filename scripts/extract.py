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