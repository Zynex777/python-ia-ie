import pandas as pd
from sklearn.preprocessing import StandardScaler

#1. carregar a base tratada na etapa anterior
ct = pd.read_csv("conversao_tipos.csv")

print("--- amostra antes da normalização ---")
print(ct.head())

#2 Separar quais calonas queremos normalizar
colunas_para_normalizar = ["idade","nota_1","nota_2"]

#3 iniciar o padronizador
scaler = StandardScaler()

#4 aplicar a normalização nas colunas escolhidas

ct[colunas_para_normalizar] = scaler.fit_transform(ct[colunas_para_normalizar])

print("\n--- Amostra após a normalização (escalonada)")
print(ct.head())
#5 salvar o arquivo 100% pronto para o treinamento no TensorFlow/keras
ct.to_csv("escala_tensorflow.csv", index=False)
print("\n Dataset esta pronto para alimentar a rede Neural")