#Faça um programa que verifique se um número é perfeito ou não.
#Um número é dito perfeito quando ele é igual a soma
#dos seus divisores excetuando ele próprio.
#(Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores).
#Exiba uma mensagem na tela informando se o número é ou não perfeito.

cont="S"
while cont=="S" or cont=="s":
    n=int(input("Número"))
    soma=0
    for i in range (1,n):
        if n % i == 0:
            soma=soma+1
    if n == soma:
        print(n,"É um número perfeito")
    else:
        print(n,"Não é um número perfeito")
    cont=str(input("Deseja continuar (S/N)?"))    
