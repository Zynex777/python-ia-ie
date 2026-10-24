# O contador começa em 1; while repete até incluir 10.
# t = t + 1 atualiza o contador e permite que a repetição termine.

numero = int(input("Qual taboada deseja: "))
t = 1

while t <= 10:
    print(f"{numero} X {t} = {numero * t}")
    t = t + 1