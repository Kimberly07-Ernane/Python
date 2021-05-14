#Faça um programa que receba dois números e que informe o tipo de cálculo
#mostre quando erro e informe o valor do cálculo.

calculo =str(input("Informe o operador (+),(-),(/),(*): "))
n=int(input("Digite um número:"))
n2= int(input(" Digite mais um número:"))

if calculo == "+":
    r = n+n2
elif calculo == "-":
    r = n-n2
    
elif calculo == "/":
    r = n/n2
    
elif calculo == "*":
    r = n*n2
else:
    print("Número ou sinal inválido")
print("O valor desse cálculo será:",r)
    
   
