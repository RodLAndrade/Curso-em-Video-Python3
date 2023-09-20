a1 = int(input("Digite o primeiro termo da progressão: "))
r = int(input("Digite a razão da progressao: "))
for c in range(0,10):
    a1 += r
    print(f"{a1} -> ", end="")
print("FIM")