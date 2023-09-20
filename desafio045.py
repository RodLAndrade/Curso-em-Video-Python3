from random import choice
from time import sleep
print("\033[1MJOCKENPÔ!\033[M")
play = str(input("Escolha entre: (1)Pedra, (2)Papel ou (3)Tesoura: "))
opcoes = ["1", "2", "3"]
robo = choice(opcoes)


if play == "1":
    print("Você escolheu Pedra.")
elif play == "2":
    print("Você escolheu Papel.")
elif play == "3":
    print("Você escolheu Tesoura.")


print("Processando escolha da maquina...")
sleep(3)


if robo == "1":
    print("A escolha da máquina é (1)Pedra!")
elif robo == "2":
    print("A escolha da máquina é (2)Papel!")
else:
    print("A escolha da máquina é (3)Tesoura!")


if  play == robo:
    print("Empate!")
elif play == "1" and robo == "2":
    print("A maquina ganhou!")
elif play == "1" and robo == "3":
    print("Você ganhou!")
elif play == "2" and robo == "1":
    print("Você ganhou!")
elif play == "2" and robo == "3":
    print("A maquina ganhou!")
elif play == "3" and robo == "1":
    print("Você perdeu!")
elif play == "3" and robo == "2":
    print("Você ganhou!")
else:
    print("Escolhe direito porra.")