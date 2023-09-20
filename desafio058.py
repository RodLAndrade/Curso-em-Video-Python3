from random import choice
print("Bem vindo ao jogo da escolha, se acertar vc ganha um parabens!")
opçoes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maquina = choice(opçoes)
bet = ""
palpites = 0
aposta = int(input("Digite um numero de 0 a 10: "))
while bet != maquina:
    aposta = int(input(f"Errou Digite um numero de 0 a 10: "))
    if aposta > 10:
        print("Digita certo caraio.")
        palpites += 1
    else:
        bet = aposta
        palpites += 1
print(f"Parabens! A escolha da maquina foi {maquina}, voce precisou de {palpites} palpites para acertar!")