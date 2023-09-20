from random import randint
from time import sleep
num = randint(0, 5)
print("Vou pensar em um número de 0 a 5, tente adivinhar...")
guess = int(input("Em qual número eu pensei? "))
if guess > 5:
    print("Os cara mete o loco mesmo né, digita certo caraio.")
else:
    print("Processando...")
    sleep(3)
    print(f"Eu pensei no número {num}.")
    if guess == num:
        print("Você acertou!")
    else:
        print("Você errou")