import csv

pessoas = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 28, "São Paulo"],
    ["Bruno", 35, "Rio de Janeiro"],
    ["Carla", 22, "Salvador"],
    ["Luis", 33, "Salvador"]
]

arquivo_pessoas = "pessoas.csv"

with open(arquivo_pessoas, mode="w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=",")
    escritor.writerows(pessoas)
