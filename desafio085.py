numeros = [[],[]]
for c in range(1,8):
    num = int(input(f"Digite o {c}º numero: "))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[1].sort()
numeros[0].sort()
print(numeros)