'''Crie um programa que gera um perfil de usuário aleatório usando a
API 'Random User Generator'. O programa deve exibir o nome, email
e país do usuário gerado."'''

import requests

url = "https://randomuser.me/api/"
response = requests.get(url)

dados = response.json()

usuario = dados["results"][0]
nome = f"{usuario['name']['first']} {usuario['name']['last']}"
email = usuario["email"]
pais = usuario["location"]["country"]

print("Nome:", nome)
print("Email:", email)
print("País:", pais)