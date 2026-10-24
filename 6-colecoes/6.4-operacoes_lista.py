# append adiciona ao final e insert insere antes do índice indicado.
# Os índices começam em zero e mudam após inserções.
# A etapa seguinte está apenas no título e permanece incompleta.

lista_inicial = ["joao", "pamela", "dominique"]
print(f"lista_inicial: {lista_inicial}")
print(60 * "-")
#-------------Acrescentando itens na lista----------------
lista_inicial.append("Eduarda")
print(f"Após o append: {lista_inicial}")
print(60 * "-")
#-------------Acrescentando itens em posicao especifica----------------
lista_inicial.insert(1, "Matheus")
print(f"Após o insert: {lista_inicial}")
print(60 * "-")
#------------Apagando indice expecifico----------------
