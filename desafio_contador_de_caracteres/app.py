# Crie um código que conta o número de vogais de um bloco de texto
# qualquer. O código deve considerar letras maiúsculas/minúsculas, 
# isto é, "a" e "A" contam da mesma forma.
# O texto pode ser colado diretamente como uma string no código.

texto = """Brandon Sanderson é um renomado escritor americano de fantasia e ficção científica,
conhecido por seus sistemas de magia detalhados, mundos ricamente construídos e tramas intricadas;
autor de sucessos como a série Mistborn e o universo Cosmere, também finalizou a saga A Roda do Tempo de
Robert Jordan, tornando-se uma figura central na literatura fantástica contemporânea e um mestre em
criar narrativas épicas que conquistam leitores no mundo inteiro."""

texto = texto.upper()

vogais = {
    'A' : 0,
    'E' : 0,
    'I' : 0,
    'O' : 0,
    'U' : 0,
}

for letra in texto:
    if letra in vogais:
        vogais[letra] += 1
total_de_vogais = sum(vogais.values())

print(f'Existe um total de {total_de_vogais} vogais no texto, sendo: ')
for k, v in vogais.items():
    print(f'{v} letras {k} no texto.')