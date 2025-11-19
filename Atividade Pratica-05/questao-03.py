'''3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.'''

valor_produto = float(input("Digite o valor do produto: "))
percentual_desconto = 1-float(input("Digite o valor percetual de desconto em decimal: "))/100

calculo_preco = lambda x, y: x*y
preco_final = calculo_preco(valor_produto, percentual_desconto)

print(f"O valor com desconto é: {preco_final:.2f}")