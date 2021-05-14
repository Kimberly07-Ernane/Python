#Faça um programa  que receba a idade de 10 pessoas
#e armazene numa lista. calcule e mostre:
#◦A quantidade de pessoas com idade superior  a  50 anos
#◦A média das idades
#◦A quantidade de pessoas com idade menor que
#◦A média das pessoas que responderam essa pesquisa.

idade=[]
const=10
for i in range(const):
    idade.append(int(input('Digite a idade: ')))

print(idade)
qtde=0
soma=0
qtd_menor=0
for i in range(const):
    if idade[i] >50:
        qtde+=1

    soma= soma + idade[i]

media= soma/const
for i in range(const):
    if idade[i]<media:
        qtd_menor+=1


print('Qtde de pessoas > 50: ',qtde)
print('Media das idades: ',media)
print('Qtde de idades < que a média: ',qtd_menor)
