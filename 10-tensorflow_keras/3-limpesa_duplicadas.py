import pandas as pd

#1. carregar o arquivo sem NaNs
dn = pd.read_csv("dados_sem_nan.csv")

#2 verificar o numero de linhas abtes de reniver as duplicadas
print(f"Total de linhas antes da limpeza de duplicadas: {len(dn)}")


#3. Diltrar e exibir apenas as linhas duplicadas
linhas_duplicadas = dn[dn.duplicated(keep=False)]
print("--- Linhas duplicadas ---")
print(linhas_duplicadas)

#4. remover linhas que sao copias fieis umas das outras
dn.drop_duplicates(inplace=True)

#5 verificar o numero de linhas apos a remoção
print(f"Total de lihas depois da limpeza de duplicadas: {len(dn)}")

#6. salvar o resultado de linhas apos a remoção
dn.to_csv("limpesa_duplicadas.csv", index=False)
