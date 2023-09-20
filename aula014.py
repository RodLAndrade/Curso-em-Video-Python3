pares = 0
impares = 0
num = ""
while num != 0:    #conhecido como condição de parada ou flag
    num = int(input("Digite um numero: "))
    if num != 0:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f"tem {impares} numeros impares e {pares} numeros pares.")
print("FIM")