from time import sleep
num = int(input("Digite um numero para saber seu fatorial: "))
c = num
f = 1
print(f"Calculando {num}!")
print(".")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print(f"{num}! = ", end="")
while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f"{f}\nFIM")
