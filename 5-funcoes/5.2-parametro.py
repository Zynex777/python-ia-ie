# frase é o parâmetro local; cada chamada fornece um argumento diferente.
# Assim, o mesmo bloco imprime os dois textos sem duplicar a função.

def imprimir(frase):
    print(frase)
frase = input("digite uma frase para imprimir: ")
imprimir(frase)
palavra = input("digite uma palavra pra imprimir: ")
imprimir(palavra)