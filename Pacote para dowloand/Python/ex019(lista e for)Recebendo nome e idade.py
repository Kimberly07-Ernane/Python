#Faça um programa que preencha uma lista com os nomes de 10 alunos,
#e outra lista com a idade dos alunos.
#Calcule e mostre :
#A quantidade de alunos que tem idade superior a 15;
#A quantidade de alunos que tem idade abaixo da média;

from random import randint
nome=[]
idade=[]
media=cont=qtd=0
for i in range(10):
    nome.append(str(input('Nome: ')))
    idade.append(randint(1,70))

media=sum(idade)/5

for i in range(10):
    if idade[i]>15:
        cont+=1

    if idade[i] < media:
        qtd+=1

print('A quantidade de alunos que tem idade superior a 15: ',cont)
print('A quantidade de alunos que tem idade abaixo da média: ',media)

