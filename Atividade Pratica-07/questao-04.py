import json

pessoas = [
    {"nome": "Mariana", "idade": 30, "cidade": "Recife"},
    {"nome": "Carlos", "idade": 25, "cidade": "Fortaleza"},
    {"nome": "Fernanda", "idade": 40, "cidade": "São Paulo"},
    {"nome": "João", "idade": 19, "cidade": "Curitiba"},
    {"nome": "Aline", "idade": 33, "cidade": "Salvador"}
]

arquivo_pessoas = "pessoas.json"

with open(arquivo_pessoas, "w", encoding="utf-8") as arquivo_json:
    json.dump(pessoas, arquivo_json, ensure_ascii=False, indent=4)

with open(arquivo_pessoas, "r", encoding="utf-8") as arquivo_json:
    dados_lidos = json.load(arquivo_json)

print("Dados lidos do arquivo:")
for pessoa in dados_lidos:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")