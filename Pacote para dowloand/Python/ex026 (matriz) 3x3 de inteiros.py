#Faça um programa que leia uma matriz 3x3 de inteiros
#e retorne a linha de maior soma.
#Imprima na tela a matriz,
#a linha de maior soma
#e a soma.

from random import randint
mat=[]
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(randint(1,10))
    mat.append(linha)

for i in range(3):
    print(mat[i])

soma_maior=sum(mat[0])
pos=0
for i in range(1,3):
    som=sum(mat[i])
    if som > soma_maior:
        soma_maior=som
        pos=i
        
print("***Maior linha***")
print (mat[pos])
print("*** A soma da maior linha***")
print(soma_maior)
