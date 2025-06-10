# Crie um programa que:
# - Peça seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá em 5 anos

print('Olá! Tudo bem contigo?')
nome = input('Qual é o seu nome? ')

print(f'Muito prazer, {nome}!')
idade = int(input(('E qual é a sua idade? ')))

print(f'{idade} anos? Que legal!')

qtd_letras_nome = len(nome)
idade_futura = idade + 5

print('Estava pensando aqui...')
print(f'Seu nome tem {qtd_letras_nome} letras e em 5 anos você terá {idade_futura} anos, sabia?')
