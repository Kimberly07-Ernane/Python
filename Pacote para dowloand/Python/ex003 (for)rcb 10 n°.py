soma=0
qtd=0
soma20=0
cont=0
media=0
for i in range(10):
    num=int(input('Entre com número: '))
    if i == 0:
        menor=num
    elif num < menor:
        menor = num

    if num % 2 == 0 and num > 10:
        soma+=num

    if num % 2==1:
        qtd+=1

    if num > 20:
        soma20+=num
        cont+=1
if cont >0:
    media=soma20/cont


print('Menor número: ', menor)
print('Soma pares e maiores  10: ',soma)
print('qtd impares: ',qtd)
print('Média maiores: ',media)

