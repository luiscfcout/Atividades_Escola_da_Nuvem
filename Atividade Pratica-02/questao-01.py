"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""

valor_real = 100.00
tx_dolar = 5.20
tx_euro = 6.155555

valor_dolar = valor_real * tx_dolar
valor_euro = valor_real * tx_euro

print(f"Valor em dólar: {valor_dolar:.2f}")
print(f"Valor em Euro: {valor_euro:.2f}")