# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo numero de
# passos no alfabeto. O numero de passos é dado por uma chave.
# Letras com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 1: = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"

# DICA: Construa 2 strings com as letras do alfabeto em ordem, 
# um para letras minusculas e outra para as maiusculas, e use 
# este string para guiar as substituições

alfabeto_maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabeto_minusculo = alfabeto_maiusculo.lower()

print('Bem vindo à cifra de cesar!')
chave = int(input('Determine a chave (deve ser um número): '))
palavra = list(input('Determine a frase a ser transformada: '))
palavra_gerada = ''

for letra in palavra:
    if letra in alfabeto_minusculo:
        posicao = alfabeto_minusculo.index(letra)
        nova_letra = alfabeto_minusculo[posicao+chave]
    elif letra in alfabeto_maiusculo:
        posicao = alfabeto_maiusculo.index(letra)
        nova_letra = alfabeto_maiusculo[posicao+chave]
    else:
        nova_letra = letra
    palavra_gerada += nova_letra

print(f'\nO termo gerado pela cifra de Cesar foi: {palavra_gerada}')