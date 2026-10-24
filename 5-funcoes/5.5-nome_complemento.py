# A função combina dois textos usando uma f-string e um espaço entre eles.
# nm e sbr são parâmetros locais; nome e sobrenome fornecem os argumentos.

def nome_completo(nm,sbr):
    return f"{nm} {sbr}"
nome = input("Qual o seu primeiro nome? ")
sobrenome = input(f"ola {nome}, qual o seu sobrenome? ")
nomecompleto = nome_completo(nome,sobrenome)
print(f"Seu nome completo é {nomecompleto}.")