#solicitando idade e se é estudante
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? s/n: ")

#validando meia entrada
meia = (idade >= 60) or estudante == "s"

#apresentando resultado ao usuario
print("Tem Direito A meia-entrada? " , meia)