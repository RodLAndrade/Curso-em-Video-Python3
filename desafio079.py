numbers = []
continuar = ""
while True:
    num = (int(input("Digite um número: ")))
    if num in numbers:
            print("Valor duplicado, não foi possível adicionar.")
    else:
        numbers.append(num)
        print(f"O número {num} foi adicionado com sucesso.")
    continuar = str(input("Quer continuar?(S/N) ")).upper().strip()
    while continuar not in "SN":
        continuar = str(input("Quer continuar?(S/N) ")).upper().strip()
    if continuar == "N":
        break
numbers.sort()
print("_" * 20)
print(f"Os valores adicionados foram: {numbers}")
print("_" * 20)