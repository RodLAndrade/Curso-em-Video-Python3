num = (int(input("Digite um numero: ")),
       int(input("Digite um numero: ")),
       int(input("Digite um numero: ")),
       int(input("Digite um numero: ")))
print(f"Os Numeros digitados foram: {num}")
print(f"O valor 9 apareceu {num.count(9)} vezes.")
par = 0
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1} posição.")
else:
    print("O numero 3 não apareceu")
for n in num:
    if n % 2 == 0:
        par += 1
if par == 0:
    print("Não tivemos numeros pares.")
else:
    print(f"Tivemos {par} numero par." if par == 1 else f"Tivemos {par} numeros pares.")