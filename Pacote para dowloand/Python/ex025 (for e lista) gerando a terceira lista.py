#Faça um programa que leia duas listas com 10 números cada.
#Gere uma terceira lista com 20 números,cujos valores deverão ser compostos
#pelos números intercalados das duas outras listas.
from random import randint
lista1=[]
lista2=[]
lista3=[]
    
for i in range (10):
    lista1.append(randint(1,20))
    lista2.append(randint(10,25))

for k in range (10):
    lista3.append(lista1[i])
    lista3.append(lista2[k])

print('Lista 1: ',lista1)
print('Lista 2: ',lista2)
print('Lista 3: ',lista3)
