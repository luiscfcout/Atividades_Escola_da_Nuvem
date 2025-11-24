'''4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
'''
par = 0
impar = 0

while True:
    entrada = input("Digite um número inteiro ou fim para encerrar: ")

    if entrada.lower() == "fim":
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            par += 1
        else:
            print(f"{numero} é ímpar.")
            impar += 1
    except ValueError:
        print("Apenas números inteiros ou fim.")

print(f"Quantidade de números pares: {par}")
print(f"Quantidade de números ímpares: {impar}")
