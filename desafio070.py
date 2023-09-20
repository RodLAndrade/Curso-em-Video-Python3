print(f"{'-'*15}\nWELKOME TO KMART\n{'-'*15}")
maisbarato = ""
menorpreco = totalcompra = maisde1000 = cont = 0
while True:
    nomeproduto = str(input("Digite o nome do produto: "))
    preço = float(input("Digite o valor do produto: R$"))
    totalcompra += preço
    cont += 1
    if cont == 1 or preço < menorpreco:
        menorpreco = preço
        maisbarato = nomeproduto
    if preço > 1000:
        maisde1000 += 1
    continuar = ""
    print(f"{'-'*15}")
    while continuar != "S" and continuar != "N":
        continuar = str(input("Quer continuar?(S/N)")).upper().strip()
    print(f"{'-' * 15}")
    if continuar == "N":
        break

print(f"O total da compra é R${totalcompra:.2f}")
print(f"{maisde1000} produtos custam mais de R$1000.00")
print(f"O produto mais barato é {maisbarato}")