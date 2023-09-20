matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maiorseg = terceirac = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f"Digite um numero para a posição [{l}, {c}]: ")))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            terceirac += matriz[l][c]
        if l == 1:
            if c == 0 or matriz[l][c] > maiorseg:
                maiorseg = matriz[l][c]
print("-="*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
print("-="*15)
print(f"A soma de todos os numeros pares digitados é {pares}")
print(f"A soma dos valores da terceira coluna é {terceirac}")
print(f"O maior valor da segunda linha é {maiorseg}")