renda = float(input("Digite a sua renda mensal: R$"))
situacao = input("Possui restrição / nome negativado? ")
emprestimo = (renda >= 3000) and situacao == "n"
print("Você pode pedir imprestimo? " , emprestimo)