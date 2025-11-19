'''4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.'''

ano = int(input("Digite o ano: "))

teste_divisao_por4 = ano % 4
teste_divisao_por100 = ano % 100
teste_divisao_por400 = ano % 400


if teste_divisao_por4 != 0:
    print("O ano não é bissexto.")
elif teste_divisao_por100 == 0 and teste_divisao_por400 != 0:
    print("O ano não é Bissexto.")
else:
    print("O ano é bissexto.")