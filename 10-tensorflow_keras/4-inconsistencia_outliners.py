import pandas as pd 
#1. carregar o arquivo limpo de duplicadas
id = pd.read_csv("limpesa_duplicadas.csv")

# --- tratamento de inconsistencia de texto ---
#1. Mostrar os valores unicos antes da limpeza
print("--- Antes da limpeza de texto ---")
print(id["status_matriculado"].unique())

#2. Padronizar: .str.strip() -remove espaços extras nas pontas
# .str.lower() - padroniza tudo para minúsculas
# .str.upper() - deixa tudo maiusculo
# .str.title() ou str.captalize() - aprenas a primeira palavra maiuscula
id["status_matriculado"] = (
    id["status_matriculado"].str.strip().str.lower()
)

#3.Mostra os valores unicos depois da limpeza
print("\n--- apos a limpeza de texto ---")
print(id["status_matriculado"].unique())


#etapa B
#1 filtra e mantem apenas os alunos com idades validas
id = id[(id["idade"] >= 16) & (id["idade"] <= 50)]

#2. corrige de forma cirurgica notas invalidas 
id.loc[id["nota_1"]>10, "nota_1"] = 10
id.loc[id["nota_1"]<0, "nota_1"] = 0

id.loc[id["nota_2"]>10, "nota_2"] = 10
id.loc[id["nota_2"]<0, "nota_2"] = 0

print("\n--- textos padronizados e outliers tratados com sucesso!")
# --- Exibindo os resultados  apos a limpeza ---
# mostra o novo painel estatistico sem idades fora do limite
print("\n--- Estatistica atualizada apos tratar os Outliers ---")
print(id.describe())

#mostrar a quantidade na tabelna apos os cortes de idade
print(f"Total de linhas validas apos os filtros {len(id)}")

#gravando a nova versao no disco
id.to_csv("limpeza_inconsistencia_outliers.csv", index=False)
print("\n Arquivo salvo com sucesso: 'limpeza_inconsistencia_outliers.csv' Criado no diretorio")