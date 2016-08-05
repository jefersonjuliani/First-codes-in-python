'''
    Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
    terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
    intercalados dos dois outros vetores. Imprima os três vetores.
'''
import random
l1= list()
l2= list()
l3= list()
for x in range(10):
    l1.append(random.randint(1,100))
    l2.append(random.randint(1,100))
l3.extend(l1)
l3.extend(l2)
print l1
print l2
print l3
