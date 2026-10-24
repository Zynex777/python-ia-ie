# As duas condições precisam ser verdadeiras: altura mínima de 1,40 m e idade mínima de 12.
# O resultado da expressão com and é um booleano.

#pedir as informacoes do usuario
altura = float(input("Qual a sua altura? (m): "))
idade = int(input("Qual a sua idade? "))
#fazer a verificacao 
permissao = (altura >= 1.40) and idade >= 12
#fala se o usuario pode ou nao andar na montanha russa
print("Você tem pormissao para andar na montanha russa? " , permissao)