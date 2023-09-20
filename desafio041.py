from datetime import date
hoje = date.today().year
ano = int(input("Digite seu ano de nascimento: "))
idade = hoje - ano
print(f"Hoje você tem {idade} anos.")
if idade <= 9:
    print("Categoria Mirim!")
elif idade <= 14:
    print("Categoria Infantil!")
elif idade <= 19:
    print("Categoria Junior!")
elif idade <= 50:
    print("Categoria Senior!")
else:
    print("Categoria Master!")