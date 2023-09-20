from random import choice
from random import randint
pcnum = count = playernum = resto = 0
playerjogada = ""
while True:
    pcnum = randint(0,10)
    playerjogada = str(input("Você quer par ou impar?(P/I) ")).upper().strip()
    while playerjogada != "P" and playerjogada != "I":
        playerjogada = str(input("Você quer par ou impar?(P/I) ")).upper().strip()
    playernum = int(input("Digite o numero: "))
    resto = (playernum + pcnum) % 2
    print(f"A maquina escolheu {pcnum} e você escolheu {playernum}")
    if resto == 0:
        print("Deu par!")
        if playerjogada == "P":
            print("Voce ganhou!")
            count += 1
        else:
            print("Voce perdeu :/ ")
            break
    else:
        print("Deu impar!")
        if playerjogada == "I":
            print("Voce ganhou")
            count += 1
        else:
            print("Voce perdeu")
            break
    print("Vamos jogar novamente!")
print(f"voce ganhou {count} vezes.")




