# A string vazia inicial permite entrar no while, que compara a entrada com "1234".
# Observe que senha_salva é lida, mas não é usada na comparação atual.

nome = input("Digite seu nome: ")
senha_salva = input("Crie uma senha: ")
senha = ""

while senha != "1234":
    senha = input("Digite sua senha: ")

print("Acesso Liberado")