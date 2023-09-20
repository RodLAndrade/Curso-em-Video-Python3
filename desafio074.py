from random import randint
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f"Os numeros sorteados foram {numeros[0]}, {numeros[1]}, {numeros[2]}, {numeros[3]}, {numeros[4]}.")
print(f"O menor numero é {min(numeros)}")
print(f"O maior numero é {max(numeros)}")

#menor = maior = 0
#for c in numeros:
#    if c == numeros[0] or c < menor:
#        menor = c
#for c in numeros:
#    if c == numeros[0] or c > maior:
#        maior = c
#print(f"O menor numero é {menor}")
#print(f"O maior numero é {maior}")