from random import choice
print("Bem vindo ao Jogo da escolha!\nA nossa inteligencia artificial escolherá um número inteiro de 1 a 5, se você acertar qual o número escolhido, você é bom, caso contrário, você é ruim.")
lista = [0,1,2,3,4,5]
num = choice(lista)
guess = int(input("Adivinhe qual o número escolhido: "))
print(f"O número escolhido foi {num}, você escolheu {guess}. ")
if guess == num:
    print("Você é bom!")
elif guess > 5:
    print("número maior que o compativel no jogo, você é pior que ruim!")
else :
    print("Você é ruim!")

print("-----------------fim de jogo-------------------------------")
