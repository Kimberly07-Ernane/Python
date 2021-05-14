#Faça um programa que  receba 3 números inteiros.
#Calcule o fatorial desses números e mostre a tela.

for i in range (3):
    n=int(input("Número: "))
    fat=1
    for k in range(2,n+1):
        fat = fat * k

    print("O fatorial de: ",n," é:", fat)
