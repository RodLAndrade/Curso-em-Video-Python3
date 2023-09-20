salario = float(input("Digite seu salario: "))
if salario > 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)
print(f"O seu salario de R${salario} vai passar a ser R${novo}")