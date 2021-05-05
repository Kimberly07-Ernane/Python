#Faça um programa que recebe dez números, calcule e mostre na tela:
# a soma dos números pares
# a quantidade de números inferiores a 10
#(com for)
soma=0
inf=0
for i in range(10):
  n=int(input('Digite um número:'))
  if n %2==0:
      soma+=n

  if n<10:
      inf+=1
      
print("Soma pares",soma)
print( "Quantidade de inferiores",inf)
