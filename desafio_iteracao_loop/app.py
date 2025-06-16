# Dado duas listas, printe todos os valores que aparecem 
# duplicados nas duas listas.

primeira_lista = ['Cachorro', 'Gato', 'Coelho', 'Raposa']
segunda_lista = ['Cachorro', 'Gato']
elementos_duplicados = []
quantidade_elementos = 0

for elemento in primeira_lista:
    for segundo_elemento in segunda_lista:
        if segundo_elemento == elemento:
            elementos_duplicados.append(segundo_elemento)
            quantidade_elementos += 1
if quantidade_elementos != 0:
    print(f'Existem {quantidade_elementos} elementos duplicados')
    print(f'Os elementos duplicados são {elementos_duplicados}')
else:
    print('Não existem elementos duplicados')