# O modo "r" abre um arquivo existente; read() lê todo o conteúdo em uma string.
# with cuida do fechamento. O caminho é relativo à pasta de execução.

with open("7-open/pessoas.txt","r",encoding="utf-8") as arquivo:
    dados = arquivo.read()
    print(dados)