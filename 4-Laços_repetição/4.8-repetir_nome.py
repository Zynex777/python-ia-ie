# O nome é lido uma vez e reutilizado nas repetições de range(qtd).
# q recebe os índices; o conteúdo impresso é sempre o valor de nome.

nome = input("Digite seu nome: ")
qtd = int(input("Imprimir quantas vezes: "))

for q in range(qtd):
    print(nome)