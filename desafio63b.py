termos = int(input("Digite quantos termos da sequencia de fibonacci quer que apareça: "))
ultimo = 1
penultimo = 0
total = 0
if termos == 0:
    print("PRA QUE DIGITOU ENTAO?")
elif termos == 1:
    print("0")
elif termos == 2:
    print("0 -> 1")
else:
    print("0 -> 1", end="")
    while termos > 2:
        total = penultimo + ultimo
        print(f" -> {total}", end="")
        termos -= 1
        penultimo = ultimo
        ultimo = total
print(" -> FIM")