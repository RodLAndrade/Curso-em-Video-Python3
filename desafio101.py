from datetime import date 
def voto(nasc):
    idade = date.today().year - nasc
    print(f"Com {idade} anos: ", end='')
    if idade < 16:
        return "Não pode votar."
    elif  16 <= idade < 18 or idade > 65:
        return "Voto facultativo."
    else: 
        return "Voto obrigatório"

ano = int(input("Digite o ano de nascimento: "))
print(voto(ano))