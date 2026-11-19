import pandas as pd
from sklearn.model_selection import train_test_split

#1 carregar a base tratada e normalizada na etapa anterior
df = pd.read_csv("escala_tensorflow.csv")

#separando as colunas do arquivo X e Y
x = df.drop(columns=["nome","id_aluno","email","nota_2"])
y = df["nota_2"]

#print("--- imprimindo as primeiras linhas do x ---")
#print(x.head(5))

#print("--- imprimindo as primeiras linhas do y ---")
#print(y.head(5))


#dividir os dados: 80% para o treino e 20% para teste
x_train, x_test, Y_train, y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
)

print("\n Dados divididos e prontos para alimentar a rede neural do TensorFlow")

#gravando os 4 arquivos usados para treino e teste da rede Neural
x_train.to_csv("x_treino.csv", index=False)
x_test.to_csv("x_teste.csv", index=False)
Y_train.to_csv("y_treino.csv", index=False)
y_test.to_csv("y_teste.csv", index=False)

print("sucesso! os arquivos foram gerados e salvos na pasta.")