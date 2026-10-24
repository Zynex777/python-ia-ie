# if e else escolhem um dos dois blocos conforme a comparação >= 18.
# capitalize() coloca a primeira letra em maiúscula e as demais em minúsculas.

nome = input("Digite seu nome: ").capitalize() ## pesquisei no google como usar o capitalize
idade = int(input("Digite sua idade: "))
if idade >= 18: ## verifica se é maior de idade ou nao(>= 18)
    print(nome , "você é maior de idade") 
else:
    print(nome , "você é menor de idade")