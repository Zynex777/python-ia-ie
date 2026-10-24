# and exige que as duas condições sejam verdadeiras: renda mínima e resposta "n".
# emprestimo guarda um booleano (True ou False), conforme a regra deste exercício.

renda = float(input("Digite a sua renda mensal: R$"))
situacao = input("Possui restrição / nome negativado? ")
emprestimo = (renda >= 3000) and situacao == "n"
print("Você pode pedir imprestimo? " , emprestimo)