from random import randint
computador = randint(0,10)
print("Tente adivinhar qual numero de 0 a 10 eu escolhi, se você acertar, ganhar um parabens!")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Digite um numero de 0 a 10: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print("Errrrrrou, chuta mais baixo.")
        else:
            print("Errrrrrou, chuta mais alto")
print(f"Minha escolha foi {computador}, voce precisou de apenas {palpites} palpites, parabens!")
