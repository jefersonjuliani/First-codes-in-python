'''
    Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
    números ímpares na lista IMPAR. Imprima as três listas.
'''
import random
l= list()
par= list()
impar= list()
for x in range(20):
    l.append(random.randint(1,100))
    if l[x] % 2==0:
        par.append(l[x])
    else:
        impar.append(l[x])
print l
print par
print impar
