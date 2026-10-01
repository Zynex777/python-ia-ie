#criando dicionario composto de cadastro de funcionario0
funcionarios = {
    "44356":{
            "nome":"Vitor Davi",
             "telefone":"11912121315",
             "data_nascimento":"10/12/2010",
             "cargo":"Jovem Aprendiz",
             "habilidade":["Front end","java","python"]
             },
    "42568":{
            "nome":"Miguel Simões",
            "telefone":"11950737479",
            "data_nascimento":"11/10/2010",
            "cargo":"Joven Aprendiz",
            "habilidade":["php","python","fl studio","gimp","linux"]
            },
    "44123":{
            "nome":"Luis cyriaco",
            "telefone":"11923837477",
            "data_nascimento":"15/3/1980",
            "cargo":"Professor e dev senior",
            "habilidade":["Html","js","css","php","python"]
            },
    "19199":{
            "nome":"Mimi Cristine",
            "telefone":"11970707070",
            "data_nascimento":"15/09/2010",
            "cargo":"Joven Aprendiz",
            "habilidade":["pacote office","python"]
    }
}
print(funcionarios["44123"])
print(funcionarios["44123"]["telefone"])