##solicitando os dados do paciente
nome = input("Qual o seu nome? ") 
peso = float(input(f"{nome}, Qual o seu peso? (kg) "))
altura = float(input(f"{nome}, Qual a sua altura? (metros) "))

#calculando o IMC do paciente
imc = peso / altura ** 2

print(f"{nome}, Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso normal")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Excesso de peso")
elif imc <= 34.9:
    print("Obesidade classe 1")
elif imc <= 39.9:
    print("Obesidade classe 2")
else:
    print("Obesidade classe 2")