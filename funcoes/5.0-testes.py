def somar(item1, item2):
    resultado = item1 + item2
    print(resultado)

def subtrair(item1, item2):
    resultado = item1 - item2
    print(resultado)

def multiplicar(item1, item2):
    resultado = item1 * item2
    print(resultado)

def dividir(item1, item2):
    if item2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = item1 / item2
        print(resultado)

pergunta1 = float(input("Digite o primeiro numero: "))
pergunta2 = float(input("Digite o segundo numero: "))

metodo = input("Digite a conta que voce quer fazer(+, -, *, /): ")

# Validação corrigida com 'not in'
while metodo not in ["+", "-", "*", "/"]:
    metodo = input("Opção inválida. Digite a conta que voce quer fazer(+, -, *, /): ")

if metodo == "+":
    somar(pergunta1, pergunta2)
elif metodo == "-":
    subtrair(pergunta1, pergunta2)
elif metodo == "*":
    multiplicar(pergunta1, pergunta2)
elif metodo == "/":
    dividir(pergunta1, pergunta2)