from datetime import date
maior = 0
menor = 0
anoatual = date.today().year
for c in range(0,4):
    ano = int(input("Digite o ano de nascimento: "))
    idade = anoatual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"{maior} pessoas são maior de idade.\n{menor} pessoas são menor de idade.")
