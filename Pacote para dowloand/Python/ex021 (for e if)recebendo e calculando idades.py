nomes=[]
idades=[]
cont=3
maior15=menor_med=0
for i in range(cont):
    nomes.append(str(input('Informe o nome do aluno: ')))
    idades.append(int(input('Informe a idade do aluno: ')))
media= sum(idades)/len(idades)
for i in range(cont):
    if idades [i]>15:
        maior15+=1
    if idades[i] < media:
        menor_med+=1
idx=idades.index(max(idades))
idx2=idades.index(min(idades))
print(f'A quantidade de alunos com idade superior  a 15 anos: {maior15}')
print(f'A média das idades  dos alunos: {media}')
print(f'A quantidade de alunois com idade abaixo da média: {media}')
print(f'A maior idade é {max(idades)} o nome do aluno {nomes[idx]}')
print(f'A menor idade é {min(idades)} o nome do aluno {nomes[idx2]}')
        
