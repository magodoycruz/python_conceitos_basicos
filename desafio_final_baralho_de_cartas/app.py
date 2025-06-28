# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:
# gerar_baralho -> retorna um baralho novo. Parâmetros da função definem quantas cópias retornar (1 baralho, 2, 3),
# se o baralho deve conter coringas e se deve ser embaralhado antes de retornado
# mostrar_baralho -> Exibe a quantidade de cartas no baralho e quais são
# dar_as_cartas -> distribui as cartas no baralho e mostra quais são
# mostrar_jogadores -> exibe a quantidade de cartas na mão de casa jogador e mostra quais são

# A partir das funções o código deve:
# - gerar o baralho e exibi-lo
# - dar as cartas aos jogadores
# - exibir o baralho após as cartas terem sido distribuídas
# - exibir a mão de cada jogador
import random

def informacoes_jogo():
    print('Primeiro, vamos configurar o baralho:')
    decks = int(input('Quantos baralhos serão utilizados: '))
    tem_coringa = verifica_resposta(input('Os baralhos terão o Coringa? S/N '))
    embaralhar = verifica_resposta(input('O baralho deve ser embaralhado antes de exibido? S/N '))
    return decks, tem_coringa, embaralhar

def verifica_resposta(resposta):
    if resposta.lower() == 's':
        return True
    if resposta.lower() == 'n':
        return False

def gerar_baralho(decks, tem_coringa, embaralhar):
    naipes = ['♦️', '♥️', '♠️','♣️']
    valores_cartas = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K']
    coringa = '🃏'
    baralho_final = []

    count = 0
    while count < int(decks):
        for naipe in naipes:
            for valor in valores_cartas:
                baralho_final.append(valor+naipe)
        count +=1
    if tem_coringa:
        baralho_final.append(coringa)
    if embaralhar:
        random.shuffle(baralho_final)
    return baralho_final  

def mostrar_baralho(baralho): #Talvez eu consiga reaproveitar para a mão dos jogadores
    print('Aqui estão todas as cartas:')
    cartas = ''
    for carta in baralho:
        cartas += carta + '     '
    print(cartas)

def dar_as_cartas(baralho):
    numero_cartas = int(input('Quantas cartas devem ser distribuídas? '))
    numero_jogadores = int(input('Quantos jogadores são? '))
    cartas_distribuidas = numero_cartas * numero_jogadores

    if cartas_distribuidas > len(baralho):
        print('Não existem cartas suficientes para todos os jogadores. Redefina os valores!')
        dar_as_cartas(baralho)
    
    jogador = 1
    maos_do_baralho = []
    while jogador <= numero_jogadores:
        cartas_selecionadas = []
        jogador += 1
        cartas = 1 #Para cada novo jogador, inicia a contagem de cartas
        while cartas <= numero_cartas:
            c = random.choice(baralho)
            cartas_selecionadas.append(c)
            baralho.remove(c)
            cartas += 1
        maos_do_baralho.append(cartas_selecionadas)
    return maos_do_baralho

def mostrar_jogadores(decks):
    decks_count = 1
    for deck in decks:
        print(f'Cartas do jogador numero {decks_count}:')
        cartas = ''
        for carta in deck:
            cartas += carta + '     '
        print(cartas)

## Execução do programa
print('Bem-vindo ao jogo de cartas! \n')

decks, coringa, embaralhar = informacoes_jogo()
baralho = gerar_baralho(decks, coringa, embaralhar)
mostrar_baralho(baralho)
decks_jogadores = dar_as_cartas(baralho)
mostrar_baralho(baralho)
mostrar_jogadores(decks_jogadores)