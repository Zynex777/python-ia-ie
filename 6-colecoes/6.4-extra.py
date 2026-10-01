import random
lista_inicial = ["joao", "pamela", "dominique"]
print(f"lista_inicial: {lista_inicial}")
print(60 * "-")
#-------------Acrescentando itens na lista----------------
print("Acrescentando itens na lista")
lista_inicial.append("Eduarda")
print(f"Após o append: {lista_inicial}")
print(60 * "-")
#-------------Acrescentando itens em posicao especifica----------------
print("Acrescentando itens em posicao especifica")
lista_inicial.insert(1, "Matheus")
print(f"Após o insert: {lista_inicial}")
print(60 * "-")
#------------Modificando item em uma lista----------------
print("Modificando item em uma lista")
lista_inicial[3] = "Rafael"
print(f"Após a modificação: {lista_inicial}")
print(60 * "-")
#------------Apagando item em indice especifico----------------
print("Apagando item em indice especifico")
del lista_inicial[3]
print(f"Após o del: {lista_inicial}")
print(60 * "-")
#-----------Apagando armazenando valor da lista----------------
print("Apagando armazenando valor da lista")
removido = lista_inicial.pop(1)
print(f"Após o pop, removido: {removido}, lista: {lista_inicial}")