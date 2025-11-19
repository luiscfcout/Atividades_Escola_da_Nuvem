'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''

import sys


modulo_temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem: (C para Celsius, F para Fahrenheit, K para Kelvin)").upper()
unidade_destino = input("Digite a unidade de destino: (C para Celsius, F para Fahrenheit, K para Kelvin)").upper()

def imprime(x, y):
    print(f"A conversão é: {x:.2f} °{y}")

if unidade_origem == unidade_destino:
    print("Não precisa conversão")
    sys.exit()
elif unidade_origem == "C" and unidade_destino == "F":
    conversao = (9 * modulo_temperatura / 5) + 32
    imprime(conversao, unidade_destino)
elif unidade_origem == "C" and unidade_destino == "K":
    conversao = modulo_temperatura + 273.15
    print(f"A conversão é: {conversao:.2f} {unidade_destino}")
elif unidade_origem == "F" and unidade_destino == "C":
    conversao = (modulo_temperatura - 32) * 5 / 9
    imprime(conversao, unidade_destino)
elif unidade_origem == "F" and unidade_destino == "K":
    conversao = (modulo_temperatura - 32) *5 / 9 + 273.15
    print(f"A conversão é: {conversao:.2f} {unidade_destino}")
elif unidade_origem == "K" and unidade_destino == "C":
    conversao = modulo_temperatura - 273.15
    imprime(conversao, unidade_destino)
elif unidade_origem == "K" and unidade_destino == "F":
    conversao = (modulo_temperatura - 273.15) * 9 / 5 + 32
    imprime(conversao, unidade_destino)
