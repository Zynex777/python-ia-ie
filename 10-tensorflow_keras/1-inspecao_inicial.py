#0-impoprtando a biblioteca pandas com o apelido pd
import pandas as pd

#1-carregar o csv sujo
db = pd.read_csv("dados_brutos.csv")

#2-inspecionar as primeiras linhas
print("---Amostra Inicial (head)---")
print(db.head())

#3-inspecionar tipos de dados e quantidades de valores nulos
print("\n---informaçoes estruturais(info)---")
print(db.info())

#4-estatisticas descritivas para ver emdias e possiveis anomalias
print("\n---informaçoes Basicas(describe)")
print(db.describe())
