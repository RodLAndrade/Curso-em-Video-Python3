from random import randint
from time import sleep
from operator import itemgetter
jogadas = dict()
ranking = dict()
for c in range(0, 4):
    jogadas[f'jogador{c}'] = randint(1, 6)
for k, v in jogadas.items():
    print(f"O {k} tirou {v} nos dados.")
    sleep(1)
print("Ranking dos jogadores: ")
ranking = sorted(jogadas.items(), key = itemgetter(1), reverse= True)
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}. ")


