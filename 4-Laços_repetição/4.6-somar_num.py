# soma é um acumulador: começa em zero e recebe cada novo valor digitado.
# range(3) repete três vezes; o print fora do laço mostra o total final.

soma = 0

for n in range(3):
    numero = float(input("Digite um número: "))
    soma = soma + numero

print(soma)