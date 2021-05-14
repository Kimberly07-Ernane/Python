#Crie um programa que receba idade e peso de cinco pessoas e calcule:
#A maior idade;
#A quantidade de pessoas que pesam mais que 90kg;
#Média das idades das pessoas que pesam menos de 50 kg.

maior=0
qtd90=0
media=0
qtd=0
soma=0
idade=int(input("Entre com a idade:"))
while idade >0:
              peso=int(input("Entre com o peso: "))
              if idade > maior:
                  msior=idade

              if peso<90:
                  qtd90+=1

              if peso <50:
                  soma = soma +idade
                  qtd+=1

              idade=int(input("Entre com a idade: "))

if qtd>0:
    media=soma/qtd
print("Maior idade:",maior)
print("Quantidade de pessoas que pesam mais que 90kg: ",qtd90)
print("Média das idades das pessoas que pasam menos que 50kg: ",media)
