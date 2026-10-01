nome = input("Digite seu nome: ").capitalize() ## pesquisei no google como usar o capitalize
i = 0
idade = int(input("Digite sua idade: "))
mensagem = "Possui Carteira de motorista?(s/n) "
while i == 0:
    possui_carteira = input(mensagem).capitalize
    if possui_carteira == "N" or "S":
        print("Digite apenas s ou n")
        mensagem = "Digite novamente se você possui carteira de motorista: "
    else: 
        i = 1
if idade >= 18: ## verifica se é maior de idade ou nao(>= 18)
    if possui_carteira == "s":
        print(nome , "você pode dirigir")
    else:
        print(nome, "você precisa de carteira de motorista para dirigir")
else:
    print(nome , "você é menor de idade")