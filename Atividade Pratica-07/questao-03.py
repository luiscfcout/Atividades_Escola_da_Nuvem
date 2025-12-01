import csv

nome_arquivo = "pessoas.csv"

with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=",")
    next(leitor)
    
    for coluna in leitor:
        print(f"Nome: {coluna[0]}, Idade: {coluna[1]}, Cidade: {coluna[2]}")