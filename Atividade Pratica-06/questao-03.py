'''3. Desenvolva um programa que consulte informações de
endereço a partir de um CEP fornecido pelo usuário,
utilizando a API ViaCEP. O programa deve exibir o
logradouro, bairro, cidade e estado correspondentes ao CEP
consultado.'''

import requests

while True:
    cep = input("Digite um CEP ou 'sair' para finalizar: ")

    if cep.lower() == "sair":
        print("Programa finalizado.")
        break

    cep = cep.strip()

    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido. Digite apenas 8 números.")
        continue

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            logradouro = dados.get("logradouro", "Não informado")
            bairro = dados.get("bairro", "Não informado")
            cidade = dados.get("localidade", "Não informado")
            estado = dados.get("uf", "Não informado")

            print("Logradouro:", logradouro)
            print("Bairro:", bairro)
            print("Cidade:", cidade)
            print("Estado:", estado)
            break

    else:
        print("Erro ao consultar a API.")