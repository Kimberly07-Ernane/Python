#Em um campeonato de futebol existem 5 times e cada um possui onze jogadores.
#Faça um programa que receba idade e o peso de cada um dos jogadores
#Calcule e mostre:
#A quantidade de jogadores com idade inferior a 18 anos;
#A média das idades dos jogadores de cada time;
#A porcentagem de jogadores com mais de 80 quilos
#entre todos os jogadores do campeonato.

time=2
jog=3
qtd_inf=total_pes=qtd80=pctg=0
for i in range(time):
    print('Time: ',i+1)
    soma=media=0
    for k in range(jog):
        idade=int(input('Digite sua idade: '))
        peso=float(input('Informe seu peso: '))
        
        
    if idade<10:
        qtd_inf+=1

    if peso>80:
        qtd80+=1


        total+=1
        total_pes+=1
        idade+= peso
    
    media=soma/jog
    print('A média das idades dos jogadores de cada time é: ',media)

    
print('A quantidade de jogadores com idade inferior a 18 anos é: ',qtd_inf)
pctg=qtd80/total_pes
print('A porcentagem de jogadores com mais de 80 quilos entre todos os jogadores do campeonato é: ',pctg)
