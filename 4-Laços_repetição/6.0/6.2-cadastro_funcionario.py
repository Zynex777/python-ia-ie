# Rascunho de dicionário aninhado, preservado no estado atual.
# Chaves repetidas sobrescrevem valores anteriores, restando a última "45623".
# A consulta a "4435" encontra uma chave ausente e causa KeyError.

# Criando dicionário de cadastro de funcionário
funcionarios = {
        "45623":{"nome": "Mimi",
         "telefone":"000088112",
         "data_nascimento":"15/09/2011",
         "cargo":"jovem Aprendiz",
          "habilidade":["pacote officie", "python"]

            },

         "45623":{"nome": "Mimi",
            "telefone":"000088112",
            "data_nascimento":"15/09/2011",
            "cargo":"jovem Aprendiz",
            "habilidade":["pacote officie", "python"]
            },
            "45623":{"nome": "Mimi",
             "telefone":"000088112",
             "data_nascimento":"15/09/2011",
             "cargo":"jovem Aprendiz",
             "habilidade":["pacote officie", "python"]
            },
}

print(funcionarios["4435"])