from time import sleep
a = [2, 3, 4, 7]
b = a
print(f"Lista 'A': {a}")
print(f"Lista 'B': {b}")
print("-"*20)
#o sinal de "=" entre as listas nao só copia como linka as duas listas, para apenas copiar usar [:] ex: b = a[:]
sleep(1)
b[2] = 8
sleep(1)
print(f"Lista 'A': {a}")
print(f"Lista 'B': {b}")
print("-"*20)
sleep(1)
b = a[:]
b[2] = 5
sleep(1)
print(f"Lista 'A': {a}")
print(f"Lista 'B': {b}")
print("-"*20)
print("FIM")

