# Crie um programa que:
# - Escolhe um número secreto
# - Pede por um chute do usuário
# - Indica se o usuário acertou ou não
# - Se não acertou dá uma dica dizendo
#   se é mais alto ou mais baixo
# - Repete isso até três vezes

import random

numero_secreto = random.randint(0,10)

count = 1 # variável auxiliar de contagem
while count<=3:
    numero_escolhido = int(input('Escolha um número de 0 a 10: '))
    if numero_escolhido == numero_secreto:
        print(f'Parabéns, você acertou o número!')
        break
    elif numero_escolhido > numero_secreto:
        print('O número é menor que o escolhido')
    else:
        print('O número é maior que o número escolhido')
    count +=1
print(f'Jogo encerrado. O número secreto era {numero_secreto}')