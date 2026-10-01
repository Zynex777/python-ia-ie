#pedir as informacoes do usuario
altura = float(input("Qual a sua altura? (m): "))
idade = int(input("Qual a sua idade? "))
#fazer a verificacao 
permissao = (altura >= 1.40) and idade >= 12
#fala se o usuario pode ou nao andar na montanha russa
print("Você tem pormissao para andar na montanha russa? " , permissao)