'''2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente,
ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False,
responda “Não”.'''

conteudo = input("Digite a frase ou palavra a ser analisada: ")
conteudo_sem_espacos = conteudo.replace(" ","").lower()
conteudo_sem_espacos_invertido = conteudo_sem_espacos[::-1]

if conteudo_sem_espacos_invertido == conteudo_sem_espacos:
    print("A palavra digitada é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")