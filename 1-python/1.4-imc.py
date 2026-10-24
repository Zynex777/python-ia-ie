# O cálculo divide o peso pela altura elevada ao quadrado. ** é potenciação.
# A altura é informada em metros; altura zero causa divisão por zero.

peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / altura**2
print("Seu IMC (Indice de Massa Corporal é: " , imc)