# desconto progressivo
valor = float(input("Qual foi o valor da sua compra? "))

if valor < 100:
    print("Sem desconto!")
elif valor <= 199.99:
    print("10% de desconto!")
else:
    print("15% de desconto!")