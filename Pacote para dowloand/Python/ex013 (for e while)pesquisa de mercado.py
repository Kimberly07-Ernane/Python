#Uma empresa fez uma pesquisa de mercado para saber se
#as pessoas gostaram ou não de um novo produto lançado no mercado.
#Para isso, forneceu o sexo do entrevistado
#e sua resposta (S – sim ou N – não).
#Sabe-se que foram entrevistadas dez pessoas.

#Faça um programa que calcule e mostre:

#O número de pessoas que responderam sim;
#O número de pessoas que responderam não;
#O número de mulheres que responderam sim;
#O número de homens que responderam não


sim=nao=0
mul_s = hom_n=0
for i in range(10):
    sexo=""
    while sexo.upper() !="F" and sexo.upper()!="M":
        sexo=str(input("Sexo (M/F): "))


    op=str(input('Gostou do produto? (S/N): '))
    if op.upper() == 'S':
        sim+=1

    if op.upper() == 'N':
        nao+=1


    if sexo.upper() == 'F' and op.upper() == 'S':
       mul_s+=1
     
    if sexo.upper() == 'M' and op.upper() == 'N':
       hom_n+=1

print('Número de pessoas  que responderam sim: ',sim)
print('Número de pessoas que responderam não: ',nao)
print('Número de mulheres que responderam sim: ',mul_s)
print('Número de homens que responderam não: ',hom_n)
