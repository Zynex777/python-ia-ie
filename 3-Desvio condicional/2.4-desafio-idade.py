nome = input("Digite seu nome: ")
idade = int(input(f"{nome}, digite sua idade: "))
if idade == 0:
    print(f"{nome}, você é recem nascido.")
elif idade < 4:
    print(f"{nome}, você é Bebe.")
elif idade < 11:
    print(f"{nome}, você é Criança.")
elif idade < 15:
    print(f"{nome}, você é Adolescente")
elif idade < 31:
    print(f"{nome}, você é Jovem.")
elif idade < 65:
    print(f"{nome}, você é Adulto.")
else:
    print(f"{nome}, você é Vintage")