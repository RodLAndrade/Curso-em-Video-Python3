salario = float(input("Digite o seu salário: "))
if salario > 1250.00:
    print(f"Você terá um aumento de 10%!\nSeu salário que é R${salario:.2f}, será aumentado para R${salario+((salario/100)*10):.2f}.")
else:
    print(f"Você terá um aumento de 15%!\nSeu salário que é R${salario:.2f}, será aumentado para R${salario+((salario/100)*15):.2f}.")