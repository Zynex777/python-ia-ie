from operacoes import somar,subtrair,multiplicar,dividir
#from arquivo_aonde_esta_as_funcoes import nomes,das,funcoes

pergunta1 = float(input("Digite o primeiro numero: "))
pergunta2 = float(input("Digite o segundo numero: "))
print(f"Soma: {somar(pergunta1,pergunta2)}")
print(f"Subtração: {subtrair(pergunta1,pergunta2)}")
print(f"Multiplicação: {multiplicar(pergunta1,pergunta2)}")
print(f"Divisão: {dividir(pergunta1,pergunta2)}")