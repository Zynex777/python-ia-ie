import pandas as pd

#1. carregando o arquivo bruto
df = pd.read_csv("dados_brutos.csv")

#2. verificar quantos valores nulos temos antes do tratamento
print("--- Valores Nulos Antes ---")
print(df.isnull().sum())

#3.preencher valores ausentes nas notas com a mediana da respectiva coluna
mediana_nota2 = df["nota_2"].median()
df["nota_2"] = df ["nota_2"].fillna(mediana_nota2)

mediana_nota1 = df["nota_1"].median()
df["nota_1"] = df ["nota_1"].fillna(mediana_nota1)

mediana_idade = df["idade"].median()
df["idade"] = df ["idade"].fillna(mediana_idade)

#4. verificar se ainda restam nulos apos o tratamento
print("--- Valores nulos depois ---")
print(df.isnull().sum())

#5. gava arquivo novo sem campos NaNs
df.to_csv("dados_sem_nan.csv", index=False)

