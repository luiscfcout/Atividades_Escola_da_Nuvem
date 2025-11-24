'''1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
'''
adicao = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao =  lambda x, y: x * y
divisao =  lambda x, y: x / y

verificador = False
while verificador == False:
    try:
        numero1 = float(input("Digite o primeiro numero: "))
        verificador = True
    except ValueError:
        print("O valor não é um numero.")
        verificador = False

verificador = False
while verificador == False:
    try:
        numero2 = float(input("Digite o segundo numero: "))
        verificador = True
    except ValueError:
        print("O valor não é um numero.")
        verificador = False

verificador = False
while verificador == False:
    operador = input("Digite o operador: ")
    verificador = True

    if operador == "+":
        total = adicao(numero1, numero2)
        print("O valor da adicao é: ", total)
    elif operador == "-":
        total = subtracao(numero1, numero2)
        print("O valor da subtração é: ", total)
    elif operador == "*":
        total = multiplicacao(numero1, numero2)
        print("O valor da multiplicação é: ", total)
    elif operador == "/":
        total = divisao(numero1, numero2)
        print("O valor da divisão é: ", total)
    else:
        print("***O valor digitado não corresponde ao operador.***")
        verificador = False