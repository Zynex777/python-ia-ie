# Média aritmética: os parênteses fazem a soma acontecer antes da divisão por 3.
# float() permite notas decimais; o exemplo não valida os limites das notas.

print("Calculadora de media dos alunos")
nome = input("digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print("a media do aluno", nome , "é", media)