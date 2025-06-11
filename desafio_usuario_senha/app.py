# Crie um programa que:
# - Pede por um nome de usuário e uma senha
# - Se ambos forem corretos, exibe uma mensagem de sucesso
# - Caso contrário, exibe uma mensagem de erro. A mensagem deve ser diferente quando o usuário está incorreto
# e quando a senha está incorreta
# - O usuario/senha "corretos" podem ser definidos como variáveis dentro do código

login = ["marcela.cruz", "123456"]

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == login[0] and senha == login[1]:
    print('Usuário logado com sucesso')
elif usuario == login[0] and senha != login[1]:
    print("Senha incorreta. Tente novamente")
elif usuario != login[0] and senha == login[1]:
    print("Usuário incorreto. Tente novamente")
else:
    print("Usuário e senha incorretos. Tente novamente")