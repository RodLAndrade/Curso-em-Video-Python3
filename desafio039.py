from datetime import date
atual = date.today().year
print("Descubra se precisa se alistar no exercito.")
ano = int(input("Digite seu ano de nascimento: "))
idade = atual - ano
print(f"Quem nasceu em {ano} tem {idade} anos hoje.")
if idade == 18:
    print("Tá na hora de se alistar mermao.")
elif idade > 18:
    print(f"Passou da hora em, vai dar ruim. Você deveria ter se alistado há {idade-18} anos, no ano de {atual-(idade-18)}.")
else:
    print(f"Ainda ta jovem, mas já já tamo ai. {18-idade} ano(s) pra você se fuder! Vai ser no ano de {atual+(18-idade)}.")
