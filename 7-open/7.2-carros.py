import csv
dados_tabela = [
    ["BAIRRO", "CIDADE", "ESTADO", "CEP"],
    ["Jardim belval","Barueri","SP","06455-000"],
    ["Parque Santana 1","Santana de Parnaíba","SP","06540-000"],
    ["Suburbano","Itapevi","SP","06600-000"],
    ["centro","Jandira","SP","06000-000"] 
]
with open("7-open/7.2-cidades.csv","w",encoding="utf-8",newline="") as arquivo_csv:
    escrevendo = csv.writer(arquivo_csv)
    escrevendo.writerows(dados_tabela)