a1 = int(input("Digite o primeiro termo da progressao aritimetica: "))
r = int(input("Digite a razão: "))
contador = 10
while contador > 0:
    print(f"{a1} -> ", end="")
    a1 += r
    contador += -1
print("FIM")