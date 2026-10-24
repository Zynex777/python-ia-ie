# A função compara a idade recebida e retorna uma descrição em texto.
# return encerra a chamada; sit guarda esse resultado para a mensagem final.

def verificar_idade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"
idade_user = int(input("Qual a sua idade? "))
sit = verificar_idade(idade_user)
print(f"Você é {sit}")