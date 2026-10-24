# while repete enquanto i == 0. Atribuir 1 a i permite encerrar as tentativas.
# A senha digitada é convertida para inteiro; letras causam ValueError.

i = 0
senha = 1234
## inventei de fazer usando while(pesquisei explicação de como usar no google e aproveitei um pré conhecimento que eu ja tinha com php)
while i == 0:
    entrada = int(input("digite a senha: "))
        ## verifica se a senha esta correta
    if entrada == senha:
        print("Senha correta, bem vindo")
        i = 1
    else:
        print("Senha incorreta, tente novamente ")
 
