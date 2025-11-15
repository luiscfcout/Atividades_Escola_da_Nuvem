"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

produto = "Camiseta"
preco = 50.00
desconto = 0.2

porcentagem_paga = 1 - desconto

total = preco * porcentagem_paga

print("ome do produto: Camiseta")
print("Preço original: R$ 50.00")
print("Porcentagem de desconto: 20%")
print("Total com desconto: ", total)