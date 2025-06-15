# Dado uma lista de palavras, print todas as palavras
# com pelo menos 5 caracteres

palavras = []
palavras_selecionadas = []

while True:
    entrada = input('Digite as palavras (digite q quando finalizar): ')
    if entrada == 'q':
        print('Ok, palavras escolhidas! Separando... \n')
        break
    palavras.append(entrada)

for palavra in palavras:
    if len(palavra) >=5:
        palavras_selecionadas.append(palavra)

print(f'As palavras com mais de 5 caracteres são: {palavras_selecionadas}')