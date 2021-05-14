#Uma empresa de ônibus precisa de um sistema para facilitar a venda de passagens.
#O ônibus possui 40 lugares e o usuário pode escolher a poltrona
#informando um número de 1 a 40,
#se a poltrona estiver ocupada deverá ser exibido uma mensagem
#informando que a poltrona já está ocupada,
#caso contrário a poltrona deve ser reservada. 
#O sistema deve ser encerrado quando for digitado zero no número da poltrona.
#No final deve ser exibido na tela:
#◦a quantidade de poltronas ocupadas
#◦a quantidade de poltronas livres
#◦Obs: deve ser usado listas para resolver este problema

#from random import sample
#p=[]
#p=sample(range(1,40),10)
#print(p)


onibus=[0]*41

p=1
p=int(input('Digite o número da poltrona: '))
while p != 0:
    if p>0 and p < 41:
        if onibus[p]==0:
            onibus[p]=1
            print('Poltrona',p, 'reservada!')
        else:
            print('Poltrona ',p, 'está ocupada!')

    else:
        print('Poltrona inválida!')


    p=int(input('Digite o número da poltrona: '))

livres=ocupadas=0
for i in range(1,40):
    if onibus[i]==1:
        ocupadas+=1

livres=40-ocupadas

print('A quantidade de poltronas ocupadas: ',ocupadas)
print('A quantidade de poltronas livres: ',livres)

