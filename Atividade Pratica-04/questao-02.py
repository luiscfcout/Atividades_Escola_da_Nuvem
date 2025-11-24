''' 2 - Criar um código que registre as notas de alunos e calcular a média da turma.
'''
notas_turma = []

while True:
    nota = input("Digite a nota, ou fim para finalizar: ")

    if nota.lower() == "fim":
        break
    elif float(nota) >= 0 and float(nota) <= 10:
        notas_turma.append(float(nota))
    else:
        print("***Digite uma nota valida.***")

media = sum(notas_turma) / len(notas_turma)
print(f"A média é {media:.2f}")