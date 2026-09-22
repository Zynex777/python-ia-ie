# caixa de atendimento
idade = int(input("Qual sua idade? "))
i = 0

while i == 0:
    # 1. Adicionado () no capitalize()
    prioridade = input("Você necessita de atendimento Prioritário? s/n ").capitalize() 
    
    # 2. Corrigido para "and"
    if prioridade != "S" and prioridade != "N":
        print("Digite apenas s/n")
    else:
        i = 1

if idade < 18:
    print("Atendimento não permitido sem responsável.")
else:
    # 3. Alterado para "S" maiúsculo (ou "s" se usar .lower())
    if prioridade == "S" or idade >= 60:
        print("Guichê 01 - Atendimento Prioritário")
    else:
        print("Guichê 02 - Atendimento Convencional")