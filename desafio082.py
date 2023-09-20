numbers = []
pares = []
impares = []
while True:
    numbers.append(int(input("Digite um número: ")))
    continuar = str(input("Continuar?(S/N) ")).upper().strip()
    if continuar == "N":
        break
for count, item in enumerate(numbers):
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
print("-=" * 30, "-")
print(f"Os numeros digitados foram: {numbers}.")
print(f"Desses, temos:\nOs pares: {pares}.")
print(f"Os impares: {impares}.")
print("-=" * 30, "-")
