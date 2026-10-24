# range(qtd) controla a quantidade de repetições, começando pelo índice zero.
# q recebe cada índice, mas não é usado na mensagem. Valores não positivos não repetem.

qtd = int(input("Digite um número: "))

for q in range(qtd):
    print("olá")
