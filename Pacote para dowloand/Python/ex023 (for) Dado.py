#Dado
from random import randint
dado=[0]*7
for i in range (10):
    n=randint(1,6)
    print('Os números que saíram foram: ',n)
    dado[n]+=1

for i in range(1,7):
    print('O número: ',i,'saiu',dado[i])
