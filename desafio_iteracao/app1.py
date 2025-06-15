# Dado uma sequência de números, calcule a soma e média dos números
# Atenção: não vale usar a função sum()

numeros = []
total = 0

while True:
    entrada = input('Escolha os números (digite q quando finalizar): ')
    if entrada == 'q':
        print('Ok, números escolhidos! Calculando... \n')
        break
    numeros.append(int(entrada))

print(f'Os números utilizados para o calculo são: {numeros}')

for numero in numeros:
    total += numero

media = total/len(numeros)
print(f'A média é {media}')