# O modo "a" acrescenta texto ao final; \n representa uma quebra de linha.
# with fecha o arquivo ao sair do bloco, inclusive em caso de exceção.
# O caminho é relativo à pasta de execução; aqui se espera a raiz do curso.

nome = input("qual seu nome? ")
email = input("qual seu email? ")
#arquivo = open("7-open/pessoas.txt", "a" , encoding="utf-8")
#arquivo.write(f"{nome} | {email}\n")
#arquivo.close()

with open("7-open/pessoas.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{nome} | {email}\n")