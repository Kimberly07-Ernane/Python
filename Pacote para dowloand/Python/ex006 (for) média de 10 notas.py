#Escreva um programa que leia 10 notas e mostre na tela a média dos alunos
#e a quantidade de alunos que tiveram nota inferior a 6.
n=0
nota = 0
rep = 0
for i in range(0,10):
    n = float(input("Informe a nota do aluno \n"))
    nota += n
    if n < 6:
        rep+=1
    
media = nota/10
print("A média das notas é:" ,media)
print("Notas reprovadas:" ,rep)
    
    
    
        
