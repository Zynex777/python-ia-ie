# Dicionários associam chaves a valores; produto["nome"] consulta uma chave.
# Uma chave ausente gera KeyError. O preço está entre aspas, portanto é texto.

#criando dicionario de produto
produto = {"nome":"requeijão","peso":"250g","validade":"20/11/2026","marca":"vigor","quantidade":5,"preco":"7.00"}
print(produto["nome"],"|",produto["preco"])