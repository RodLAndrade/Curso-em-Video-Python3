numeros = "Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"
print("-"*20)
guess = int(input("Digite um numero de 1 a 20: "))
while guess < 0 or guess > 20:
    guess = int(input("Tente novamente, digite um numero de 1 a 20: "))
print(f"{'-'*20}\nVoce digitou o numero {numeros[guess]}.\n{'-'*20}")