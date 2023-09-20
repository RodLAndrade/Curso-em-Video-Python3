a1 = int(input("Digite o primeiro termo da progressão aritimética: "))
r = int(input("Digite a razao: "))
contador = 10
continuar = ""
total = 0
while continuar != 0:
    while contador > 0:
        print(f"{a1}", end=" ")
        print(" -> " if contador > 1 else " ...", end="")
        a1 += r
        contador -= 1
        total += 1
    continuar = int(input("\nQuantos termos a mais voce quer mostrar?  "))
    contador += continuar
print(f"Foram visualizados {total} termos.")
print("FIM.")
