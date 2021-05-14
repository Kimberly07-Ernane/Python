#crie um programa que receba cinco números
#e some somente os número primos.

soma=0
for i in range (5):
    n=int(input("Número: "))
    cont_div=0
    for k in range (1,n+1):
        if n % k == 0:
            cont_div+=1


    if cont_div ==2:
        soma=n
        print("Primo: ",n)

print("Soma dos primos ",soma)
