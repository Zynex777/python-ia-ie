# or resulta em True quando pelo menos uma condição é verdadeira.
# >= inclui o limite e == compara valores. A resposta é comparada exatamente com "s".

#solicitando idade e se é estudante
idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante? s/n: ")

#validando meia entrada
meia = (idade >= 60) or estudante == "s"

#apresentando resultado ao usuario
print("Tem Direito A meia-entrada? " , meia)