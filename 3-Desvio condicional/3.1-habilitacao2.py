nome = input("Digite seu nome: ").capitalize() ## pesquisei no google como usar o capitalize
idade = int(input("Digite sua idade: "))
possui_carteira = input("Possui Carteira de motorista?(s/n) ")
if idade >= 18: ## verifica se é maior de idade ou nao(>= 18)
    if possui_carteira == "s":
        print(nome , "você pode dirigir")
    else:
        print(nome, "você precisa de carteira de motorista para dirigir")
else:
    print(nome , "você é menor de idade")