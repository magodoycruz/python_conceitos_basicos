# Dado uma sequência de números, calcule o maior valor da sequência.
# Atenção: não vale usar a função max()

numeros = []
maior = 0

while True:
    entrada = input('Escolha os números (digite q quando finalizar): ')
    if entrada == 'q':
        print('Ok, números escolhidos! Encontrando o maior... \n')
        break
    numeros.append(int(entrada))

for numero in numeros:
    if numero > maior:
        maior = numero

print(f'O Maior número é: {maior}')