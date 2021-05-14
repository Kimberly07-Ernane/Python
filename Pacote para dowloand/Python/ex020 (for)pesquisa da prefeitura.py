#A prefeitura de uma cidade fez uma pesquisa entre 10 habitantes, coletando dados sobre o salário e o número de filhos, armazene os salários e número de filhos em listas. Faça um programa que calcule e mostre:
#◦média de salário da população;
#◦média do número de filhos;
#◦maior salário;
#◦percentual de pessoas com salário inferior a R$ 1000,00.
from random import randint
sal=[]
filhos=[]
med_sal=media_filhos=maior=cont=perc=soma=som_f=0
for i in range (10):
    sal.append(randint(800,2500))
    filhos.append(randint(0,5))
    soma+=sal[i]
    soma_f+=filhos[i]           

med_sal=soma/10
med_filhos=soma_f/10
maior=sal[0]

for i in range(10):
    if sal[i]<1000:
        cont+=1

    if sal[i]>maior:
        maior=sal[i]

perc=(cont/10)*100

print('Média de salário da população: ',med_sal)
print('Média do número de filhos: ',med_filhos)
print('Maior salário: ',maior)
print('percentual de pessoas com salário inferior a R$ 1000,00.',perc)
