# random.choice() escolhe um item de uma sequência não vazia, sem removê-lo.
# return entrega o item sorteado para o print() externo.

import random
def sortear(lista):
    return random.choice(lista)

lista = ["arroz", "feijão", "nada", "sprite"]
print(lista)
print(sortear(lista))