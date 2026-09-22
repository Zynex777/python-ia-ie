import random
def sortear(lista):
    return random.choice(lista)

lista = ["arroz", "feijão", "nada", "sprite"]
print(lista)
print(sortear(lista))