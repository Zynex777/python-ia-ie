nome = input("Qual o seu nome? ")
nota1 = float(input(f"{nome}, qual foi sua primeira nota? "))
nota2 = float(input(f"{nome}, qual foi sua segunda nota? "))
nota3 = float(input(f"{nome}, qual foi sua terceiera nota? "))
nota4 = float(input(f"{nome}, qual foi sua quarta nota? "))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media < 4:
	situacao = "Reprovado"
elif media <= 6:
	situacao = "Recuperação"
else:
	situacao = "Aprovado"
print(f"A Media do aluno(a) {nome} é {media:.2f}, ele esta: {situacao}")