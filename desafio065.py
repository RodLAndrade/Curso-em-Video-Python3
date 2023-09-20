comando = ""
total = cont = media = maior = menor = 0
while comando != "N":
    num = int(input("Digite um numero: "))
    total += num
    cont += 1
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    comando = str(input("Quer continuar?(S/N) ")).upper()
    while comando != "S" and comando != "N":
        print("Digita certo caraio.")
        comando = str(input("Quer continuar?(S/N) ")).upper()
media = total / cont
print(f"Foram digitados {cont} numeros.\nO menor numero foi {menor} e o maior foi {maior}.\nO total foi {total} e a media é {media}.\nFIM")