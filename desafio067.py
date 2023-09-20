tab = total = 0
while True:
    tab = int(input("Digite o numero da tabuada que deseja: "))
    print("-" * 30)
    if tab < 0:
        break
    for c in range (0, 11):
        total = tab * c
        print(f"{tab} x {c} = {total}")
    print("-" * 30)
print("FIM")