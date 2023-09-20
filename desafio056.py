mulheres = 0
idoso = ""
idadeidoso = 0
idadetotal = 0
homens = 0
for c in range(1, 5):
    nome = str(input(f"Digite o nome da {c}ª pessoa: "))
    idade = int(input(f"Digite a idade da {c}ª pessoa: "))
    sexo = str(input(f"Digite o sexo da {c}ª pessoa (M/F): ")).upper()
    idadetotal += idade
    if c == 1 and sexo == "M":
        idoso = nome
        idadeidoso = idade
        homens += 1
    else:
        if idade > idadeidoso and  sexo == "M":
            idadeidoso = idade
            idoso = nome
        if sexo == "F":
            mulheres += 1
if homens == 0:
    print("Não há homens na lista.")
else:
    print(f"O homem mais idoso é {idoso}.")
media = idadetotal/4
print(f"A idade média das pessoas é {media:.0f} anos.")
print(f"São no total {mulheres:.0f} mulheres.")
