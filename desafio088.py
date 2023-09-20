from random import randint
from time import sleep
jogos = []
jog = []
print("=-" * 20)
p = "RANDOMIZADOR MEGA-SENA"
print("{:^20}".format(p))
print("=-" * 20)
quantidade = int(input("Quantos jogos deseja sortear: "))
for j in range(0, quantidade):
    while len(jog) < 6:
        num = randint(1, 60)
        if num not in jog:
            jog.append(num)
    jog.sort()
    jogos.append(jog[:])
    jog.clear()
for count, item in enumerate(jogos):
    print(f"Jogo {count+1}: {item}")
    sleep(1)
print("=-" * 20)



