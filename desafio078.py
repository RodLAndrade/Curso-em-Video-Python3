numeros = []
maior = menor = 0
print("-=-"*15)
for c in range(0, 5):
    numeros.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0 or menor > numeros[c]:
        menor = numeros[c]
    if c == 0 or maior < numeros[c]:
        maior = numeros[c]
print("-=-" * 15)
print(f"Você digitou os números: {numeros}")
print(f"O maior é {maior} e apareceu nas posições: ",end="")
for count, item in enumerate(numeros):
    if item == maior:
        print(f"{count}... ",end="")
print(f"\nO menor é {menor} e apareceu nas posições: ",end="")
for count, item in enumerate(numeros):
    if item == menor:
        print(f"{count}... ",end="")
print("-=-" * 15)
print("\nFIM")
