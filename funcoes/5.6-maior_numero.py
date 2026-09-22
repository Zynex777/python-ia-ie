def maior_numero(x,y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "Numeros iguais."

numero1 = float(input("Digite o Primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
maior = maior_numero(numero1,numero2)
if maior == "Numeros iguais.":
    print(maior)
else:
    print(f"O maior numero é {maior}")