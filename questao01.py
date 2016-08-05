'''
    Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
    as funcoes max e min.
'''
import random
minimo =100
maximo = 0
lista = list()
for x in range(10):
    lista.append(random.randint(1,100))
    if lista[x]< minimo:
        minimo = lista[x]
    if lista[x]>maximo:
        maximo = lista[x]
print lista
print maximo
print minimo
'''
l = [1,2,3,4,5]
print max(l)
print min(l)
'''
