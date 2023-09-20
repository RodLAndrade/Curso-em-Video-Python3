termo = int(input("Digite o termo que deseja na sequencia fibonnaci: "))
if termo == 1 or termo == 2:
    print("1")
else:
    ultimo = 1
    penultimo = 1
    total = 0
    count = 3
    while count <= termo:
        total = ultimo + penultimo
        count += 1
        penultimo = ultimo
        ultimo = total
    print(total)


