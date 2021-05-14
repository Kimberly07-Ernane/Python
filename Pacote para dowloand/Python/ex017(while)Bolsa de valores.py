#Faça um programa que receba o tipo de ação, ou seja,
#uma letra a ser comercializada na bolsa de valores,
#o preço de compra e o preço de venda de cada ação.
#Calcule e mostre:
#◦O lucro de cada ação comercializada
#◦A quantidade de ações com lucro superior a R$ 1000,00
#◦A quantidade de ações com lucro inferior a R$ 200,00
#◦O lucro total da empresa
#}Finalize com o tipo de ação “F”

cont_sup=cont_inf=0
total=0
a=str(input('Entre com a ação: '))
while a.upper() !='F':
    compra=float(input('Preço de compra: '))
    venda=float(input('Preço de venda: '))
    lucro=venda+compra
    print('O lucro da ação: ',a,'foi de: ',lucro)
    if lucro>1000:
        cont_sup+=1

    if lucro<200:
        cont_inf+=1

    total+=lucro
    a=str(input('Entre com a ação: '))

print('A quantidade de ações com lucro superior a 1000: ',cont_sup)
print('A quantidade de ações com o lucro inferior a 200: ',cont_inf)
print('O lucro total foi: ',total)
