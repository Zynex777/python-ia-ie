# Soma de dois valores. input() devolve texto e float() converte para número decimal.
# A conversão também aceita inteiros; texto não numérico causa ValueError.

#solicitando 2 numeros ao usuario
numero_1 = float(input("Digite um numero: "))# o float() converte o input para aceitar apenas float
numero_2 = float(input("digite outro numero: "))
resultado = numero_1 + numero_2
print("a soma de " , numero_1 , " + " , numero_2 , " é " , resultado)