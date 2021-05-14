#Faça um programa que receba vários números, calcule e mostre:
#A soma dos números digitados
#A média dos números digitados
#O maior dos números múltiplos de 3
#A quantidade de números primos
#A quantidade de números multiplos de 5
#finalize a entrada digitando o número zero ou negativo
soma=soma3=qtd3=qtd5=media=qtd=maior=qtd_pri=0
n=int(input('Digite um número: '))
while n > 0:
    soma+=n
    qtd+=1 #quantidade de números informados
    if qtd == 1:
        maior=n
    elif n > maior:
        maior=n

    if n % 3 == 0:
        soma3+=n
        qtd3+=1

    if n % 5 == 0:
        qtd5+=1

    div=0
    for k in range(1,n+1):
        if n % k == 0:
            div+=1

    if div == 2:
        qtd_pri+=1
        
    n=int(input('Digite um número: '))


if qtd > 0:
    media=soma/qtd

if qtd3 > 0:
    med_3=soma3/qtd3

print('A soma dos números digitados: ',soma)
print('A média dos números digitados: ',media)
print('A quantidade de números primos: ',qtd_pri)
print('A quantidade de números multiplos de 5: ',qtd5)

