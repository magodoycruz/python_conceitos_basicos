# Pegando o ultimo elemento de uma lista (conta a lista de trás pra frente):
lista = ['elemento 1', 'elemento 2', 'elemento 3']
print(lista[-1])

tupla = (1,2,3) # "versão" imutável de listas
lista_em_tupla = tuple(lista) #transforma lista em tupla
tupla_em_lista = list(tupla) # transforma tupla em lista

# Slicing - Inclui o primeiro termo, mas não o segundo
pessoas = ['João', 'Paulo', 'Clara', 'Maria']
print(pessoas[1:3]) #Paulo, Clara

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sequencia = list(range(1,5)) #[1, 2, 3, 4]
sequencia_par = list(range(0,10,2)) #[0, 2, 4, 6, 8]