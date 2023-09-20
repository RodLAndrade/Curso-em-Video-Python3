from random import choice
print("Bem vindo ao Jogo da escolha!\nA nossa inteligencia artificial escolherá um número inteiro de 1 a 5, se você acertar qual o número escolhido, você é bom, caso contrário, você é ruim.")
lista = [1,2,3,4,5]
num = choice(lista)
guess = int(input("Adivinhe o numero de 1 a 5 escolhido: "))
print(f"O numero escolhido foi {num}, você escolheu {guess}.")
print("Você é bom!" if guess == num else "Você é ruim!\n----------------------FIM----------------------")
