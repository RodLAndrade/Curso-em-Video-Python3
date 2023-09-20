numbers = []
while True:
    numbers.append(int(input("Digite um número: ")))
    continuar = str(input("Quer continuar?(S/N) ")).upper().strip()
    while continuar not in "SN":
        continuar = str(input("Quer continuar?(S/N) ")).upper().strip()
    if continuar == "N":
        break
numbers.sort()
numbers.reverse()
print("-="*30,"-")
print(f"No total foram digitados {len(numbers)} números.")
print(f"Os números digitados foram: {numbers}")
if 5 in numbers:
    print("O número 5 está na lista!")
else:
    print("O número 5 não está na lista :/")
print("-="*30,"-")