# if/elif/else selecionam uma mensagem conforme a faixa de valor da compra.
# O exemplo informa a porcentagem, sem calcular o desconto ou o preço final.

# desconto progressivo
valor = float(input("Qual foi o valor da sua compra? "))

if valor < 100:
    print("Sem desconto!")
elif valor <= 199.99:
    print("10% de desconto!")
else:
    print("15% de desconto!")