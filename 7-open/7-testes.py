# O arquivo é aberto para acrescentar dados, fechado e reaberto para leitura.
# write() grava texto; read() lê a partir da posição atual; close() fecha o arquivo.
# Os caminhos usados pressupõem execução a partir da raiz do curso.

nome = input("qual seu nome? ")
email = input("qual seu email? ")
arquivo = open("7-open/pessoas.txt", "a", encoding="utf-8")
arquivo.write(f"{nome} | {email}\n")
arquivo.close()
arquivo = open("7-open/pessoas.txt", "r",encoding="utf-8")
print(arquivo.read())
arquivo.close()