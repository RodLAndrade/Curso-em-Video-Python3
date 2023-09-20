num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
num3 = int(input("Digite mais um numero: "))
num4 = int(input("Digite um ultimo numero: "))
numeros = num1, num2, num3, num4
pares = nove = tres = 0
print(f"Os numeros digitados foram: {numeros}")
for c in numeros:
    if c == 9:
        nove += 1
    if c == 3:
        tres = (numeros.index(c)) + 1
    if c % 2 == 0:
        pares += 1
if nove == 0:
    print("O numero nove não apareceu.")
else:
    print(f"O numero nove apareceu {nove} vezes.")
if tres == 0:
    print("O numero tres não apareceu.")
else:
    print(f"O numero tres apareceu na {tres}ª posição.")
if pares == 0:
    print("Não tem numeros pares.")
else:
    print(f"Foram digitados {pares} numeros pares.")