import pandas as pd
#1. Carregar a nova base de dados tratada na etapa anterior
li = pd.read_csv("limpeza_inconsistencia_outliers.csv")

print("--- Antes do encoding (status_matriculado)")
print(li["status_matriculado"].head())

#trandormando textos em numeros binarios (0 e 1)
li["status_matriculado"] = li["status_matriculado"].map({"sim":1,"não":0})

print("--- Após o Encoding (status_matriculado)")
print(li["status_matriculado"].head())

#salvando o resultado final para o TensorFLow
li.to_csv("conversao_tipos.csv", index=False)
print("\n Variaveis codificadas e arquivo final salvo com sucesso!")