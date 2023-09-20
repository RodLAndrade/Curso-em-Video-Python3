numeros = "Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
print("-"*20)
while True:
    while True:
        guess = int(input("Digite um numero de 0 a 20: "))
        if guess > 0 or guess < 20:
            break
        print("Tente novamente.", end="")
    print(f"Você digitou o numero {numeros[guess]}.")
    while True:
        continuar = str(input("Quer continuar?(S/N) ")).upper().strip()
        if continuar in "SN":
            break
    if continuar == "N":
        break
print("FIM")
