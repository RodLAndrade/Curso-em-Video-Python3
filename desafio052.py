numero = int(input("Digite um numero: "))
divisiveis = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f"\033[32m{c}\033[m", end=' ')
        divisiveis += 1
    else:
        print(f"\033[31m{c}\033[m", end=' ')
if divisiveis > 2 or divisiveis == 1:
    print("\nNão é primo.")
else:
    print("\nÉ primo.")