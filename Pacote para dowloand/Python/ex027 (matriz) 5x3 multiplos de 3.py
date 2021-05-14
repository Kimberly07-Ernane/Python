#Faça um programa que preencha uma matriz 5 x 3,
#calcule e mostre:
#◦A quantidade de números da matriz que são múltiplos de 3
#◦A soma dos números que são pares e maiores que 10
#◦A média de números que estão armazenados na matriz.
from random import randint
mat=[]
for i in range(5):
    linha=[]
    for k in range(3):
        linha.append(randint(1,15))
    mat.append(linha)

qtd=soma=total=media=0
for i in range(5):
    for k in range(3):
        if mat[i][k]% 3 == 0:
            qtd+=1
            
        if mat[i][k]% 2 == 0 and mat[i][k] >10:
            soma+=mat[i][k]
            
        total+=mat[i][k]

media=total/15

for i in range(5):
    print(mat[i])

print('Quantidade de múltiplos de três: ',qtd)
print('Soma dos números pares: ',soma)
print('Média dos números que estão armazenados na matriz: ',media)

               
