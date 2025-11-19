'''4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.'''

from datetime import date
nascimento = []
data_sistema = date.today()

nascimento.append(int(input("Digite o ano de nascimento: ")))
nascimento.append(int(input("Digite o mês de nascimento: ")))
nascimento.append(int(input("Digite o dia de nascimento: ")))

nascimento_formatado = date(nascimento[0], nascimento[1], nascimento[2])

temp_diferenca = data_sistema - nascimento_formatado
print(f"Você está vivo há",temp_diferenca.days,"dias." )