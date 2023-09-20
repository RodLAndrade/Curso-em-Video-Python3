from random import randint
from time import sleep
numeros = list()

def sorteio(lista):
    print("Sorteando 5 valores para a lista:")
    for c in range(0, 5):
        num = randint(0, 9)
        print(f"{num} ", end='', flush=True)
        sleep(0.5)
        lista.append(num)
    print("Pronto!")

def somaPar(lista):
    pares = 0
    for  v in lista:
        if v % 2 == 0:
            pares += v
    print(f"Somando os valores pares de {numeros}, temos {pares}.")


sorteio(numeros)
somaPar(numeros)
    