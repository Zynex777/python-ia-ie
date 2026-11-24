import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from tensorflow import keras
#==============================
# 1. Carregar os dados de teste
#==============================
print("--- carregando dados de teste ---")
x_test = pd.read_csv("x_teste.csv")
y_test = pd.read_csv("y_teste.csv")
#=====================================
# 2. Carregar o cerebro da ia ja salva
#=====================================
print("--- Carregando o modelo ja salvo (.keras) ---")
modelo_preditivo = keras.models.load_model("analizador_notas_v3_19112026.keras")
print("--- Modelo carregado com sucesso na memoria do computador ---")
#====================================
# 3. avaliar o modelo (a prova final)
#====================================
print("\n--- Avaliando a IA com os dados que ela nunca viu ---")
resultado_teste = modelo_preditivo.evaluate(x_test,y_test)
print(f"perda (loss) oficial do teste: {resultado_teste}")

#====================================
# 4. FAZER uMA RESUSAO COM ALUNO NOVO
#====================================
print("\n--- Fazendo uma previsão real ---")
# pegando apenas o primeiro aluno de base de teste para simular um caso real
aluno_exemplo = x_test.head(1)
nota_real = y_test.head(1)
#a ia faz a revisao
previsao = modelo_preditivo.predict(aluno_exemplo)

print(f"dados dos analizado: \n{aluno_exemplo}")
print(f"nota real (gabarito): {nota_real}")
print(f"nota prevista pela IA: {previsao[0][0]:.2f}")