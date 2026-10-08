nome = input("qual seu nome? ")
email = input("qual seu email? ")
#arquivo = open("7-open/pessoas.txt", "a" , encoding="utf-8")
#arquivo.write(f"{nome} | {email}\n")
#arquivo.close()

with open("7-open/pessoas.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{nome} | {email}\n")