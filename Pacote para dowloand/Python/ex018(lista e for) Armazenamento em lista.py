#faça um programa que receba 10 números inteiros e armazene numa lista.
#Calcule e mostre:
#A quantidade de números pares;
#A soma dos números ímpares;
#A quantidade de números entre 10 e 20(inclusive);
#A média dos números da lista.

from  random import randint
n=[]
for i in range(10):
    n.append(randint(10,20))
    print(n)
par=impar=qtd=soma=media=0
for i in range(10):
    if n[i]%2==0:
        par+=1

    else:
        impar+=n[i]

    if n[i]>=10 and n[i]<=20:
        qtd+=1

    soma+=n[i]

media=soma/len(n)  
print('Quantidade de números pares: ',par)
print('A soma dos números ímpares: ',impar)
print('A quantidade de números entre 10 e 20: ',qtd)
print('A média dos números da lista: ',media)
