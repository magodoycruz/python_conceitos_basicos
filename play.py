# Pegando o ultimo elemento de uma lista (conta a lista de trás pra frente):
lista = ['elemento 1', 'elemento 2', 'elemento 3']
#print(lista[-1])

tupla = (1,2,3) # "versão" imutável de listas
lista_em_tupla = tuple(lista) #transforma lista em tupla
tupla_em_lista = list(tupla) # transforma tupla em lista

# Slicing - Inclui o primeiro termo, mas não o segundo
pessoas = ['João', 'Paulo', 'Clara', 'Maria']
#print(pessoas[1:3]) #Paulo, Clara

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sequencia = list(range(1,5)) #[1, 2, 3, 4]
sequencia_par = list(range(0,10,2)) #[0, 2, 4, 6, 8]

# Dicionarios
capitais = {
    'Brasil': 'Brasilia', 
    'França': 'Paris', 
    'Japão': 'Tóquio'
}
#print(capitais['Brasil'])
#print('Brasil' in capitais)

#print(capitais.get('Inglaterra', 'Não foi encontrado')) # Se não encontrar o valor, retorna uma mensagem ou valor default

def dividir(a, b):
    if b == 0:
        return 'Impossível dividir!'
    else:
        return a / b

print(dividir(b=10, a=0)) #Como os argumentos foram declarados com as suas respectivas variaveis, o valor é identificado
print(dividir(10, 0)) #Atribui os argumentos na ordem dos parâmetros