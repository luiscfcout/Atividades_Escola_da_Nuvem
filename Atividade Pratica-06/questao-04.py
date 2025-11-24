'''4. Crie um programa que consulte a cotação atual de uma
moeda estrangeira em relação ao Real Brasileiro (BRL). O
usuário deve informar o código da moeda desejada (ex: USD,
EUR, GBP), e o programa deve exibir o valor atual, máximo e
mínimo da cotação, além da data e hora da última
atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação.'''

import requests

while True:
    moeda = input("Digite o código da moeda em USD, EUR, GBP ou sair: ")

    if moeda.lower() == "sair":
        print("fim.")
        break

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        chave = f"{moeda}BRL"

        if chave in dados:
            cotacao = dados[chave]
            atual = cotacao["bid"]
            maximo = cotacao["high"]
            minimo = cotacao["low"]
            data_hora = cotacao["create_date"]

            print(f"Moeda: {moeda}/BRL")
            print(f"Valor atual: R$ {atual}")
            print(f"Valor máximo: R$ {maximo}")
            print(f"Valor mínimo: R$ {minimo}")
            print(f"Última atualização: {data_hora}")
            print("-" * 40)
        else:
            print("Moeda não encontrada. Verifique o código informado.")
    else:
        print("Erro ao consultar a API.")