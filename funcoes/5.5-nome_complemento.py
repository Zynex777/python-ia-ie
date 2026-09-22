def nome_completo(nm,sbr):
    return f"{nm} {sbr}"
nome = input("Qual o seu primeiro nome? ")
sobrenome = input(f"ola {nome}, qual o seu sobrenome? ")
nomecompleto = nome_completo(nome,sobrenome)
print(f"Seu nome completo é {nomecompleto}.")