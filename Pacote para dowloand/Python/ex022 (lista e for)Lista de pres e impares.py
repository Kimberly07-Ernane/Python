#Faça um programa que leia 10 números inteiros e armazene-os numa lista
#Armazene os números pares na lista PAR e os números impares na lista IMPAR.
#Imprima as três listas
from random import randint
num=[]
pares=[]
impares=[]

for x in range (10):
  num.append(randint(1,50))

  if num[x] %2==0:
      pares.append(num[x])
  else:
      impares.append(num[x])
print('A lista de números é:  ',num)
print('Os números pares são: ',pares)
print('Os números impares são: ',impares)
