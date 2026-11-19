import pandas as pd
import tensorflow as tf
from tensorflow import keras
#=================================================================
#carregamento dos dasdos de treinamento da inteligencia tensorflow
#=================================================================

print("--- 1. Carregando os dados ---")
x_train = pd.read_csv("x_treino.csv")
x_test = pd.read_csv("x_teste.csv")
y_train = pd.read_csv("y_treino.csv")
y_test = pd.read_csv("y_teste.csv")

#=================================================================
#DESENHANDO A ESTRUTURA DO NOSSO MODELO DE INTELIGENCIA TENSORFLOW
#=================================================================

#1 modelo subsequential e os neuronios (o desenho da planta basica)

modelo = keras.Sequential(
    [
    #2 primeira camada : 10 neuronios que recebem as colunas de entrada (x_train)
    keras.layers.Dense(10, activation="relu", input_shape=[x_train.shape[1]]),
    #camada de saida: 1 neuronio para prever a nota_2
    keras.layers.Dense(1)
    
    ]
)

#3. as regras de Erro e otimizaçãp (o .compile)
modelo.compile(
    optimizer="adam",
    loss="mse"
)

#=================================================================
#TREINAMENTO DA INTELIGENCIA ARTIFICIAL (A aula pratica)
#=================================================================
print("--- iniciando o treinamento da inteligencia artificial ---")

#o metodo .fit é onde a magia acontece: entregamos as pistas e o gabarito
historico = modelo.fit(
    x_train,
    y_train,
    epochs=10, #quantas voltas (épocas) e IA vai ler e reeestudar toda a base de dados
    verbose=1 #exibe a barra de progresso no terminal a cada ciclo
)
print("Treinamento concluido")

#=================================================================
#SALVANDO O MODELO TREINADO
#=================================================================
print ("\n--- Salvando o cerebro da ia em arquivo")
modelo.save("analizador_notas_v3_19112026.keras")
print("modelo salvo com sucesso como analizador_notas_v3_19112026.keras")