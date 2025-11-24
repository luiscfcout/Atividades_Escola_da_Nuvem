'''3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.'''

while True:
    senha = input("Digite uma senha ou sair para finalizar: ")

    if senha.lower() == "sair":
        break
    
    tamanho = len(senha) >= 8

    numero = any(char.isdigit() for char in senha)

    if tamanho and numero:
        print("Senha forte")
        break
    elif tamanho and not numero:
        print("***Não tem um numero.***")
    elif not tamanho and numero:
        print("***Não contem tamanho suficiente.***")
    else:
        print("Senha fraca. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")