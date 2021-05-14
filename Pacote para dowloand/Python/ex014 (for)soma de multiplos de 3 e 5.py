#Faça um programa que receba dez números, calcule e mostre na tela:
#A soma dos números múltiplos de 3 a 5
#A média dos números que estão no intervalo entre 10 e 30

from random import randint
soma = tot= cont = media = 0 
for i in range(10):
    n=randint(1,30)
    print(n)
    if n % 3 == 0 and n % 5 == 0:
        soma+=n

    if n>= 10 and n<= 30:
        tot +=n
        cont+=1

if cont > 0:
   media= tot/cont

print('Soma dos multiplos de 3 e 5: ',soma)
print('A média de números entre 10 e 30: ',media)
