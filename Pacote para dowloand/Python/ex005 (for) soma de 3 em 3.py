#Escreva um programa para encontrar a soma
#S = 3 + 6 + 9 +…. + 333.

S = 0
for i in range(3, 334, 3):
    S = S + i
    print('soma: ', S)

