from datetime import datetime

# Obtém a data e hora atual do sistema
agora = datetime.now()

# Extrai o dia, mês e ano
dia = agora.day
mes = agora.month
ano = agora.year
nome = input("Qual seu nome? ")
nas_dia = int(input(f"{nome}, qual dia você nasceu? "))
nas_mes = int(input(f"{nome}, qual mes você nasceu? "))
nas_ano = int(input(f"{nome}, qual ano você nasceu? "))
idade_aprox = ano - nas_ano
print(f"idade aproximada: {idade_aprox}")
if mes < nas_mes and dia < nas_dia:
    idade = idade_aprox - 1
else:
    idade = idade_aprox
print(f"{nome}, sua idade é: {idade}")
if idade == 0:
    print(f"Você é recem nascido.")
elif idade < 4:
    print(f"Você é Bebe.")
elif idade < 11:
    print(f"Você é Criança.")
elif idade < 15:
    print(f"Você é Adolescente")
elif idade < 31:
    print(f"Você é Jovem.")
elif idade < 65:
    print(f"Você é Adulto.")
else:
    print(f"Você é Vintage")