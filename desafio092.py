from datetime import date
cadastro = {}
cadastro['nome'] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
cadastro['idade'] = date.today().year - nasc
cadastro['ctps'] = int(input("Carteira de Trabalho (0 nao tem): "))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input("Ano de contratação: "))
    cadastro['salário'] = float(input("Salário: R$"))
    cadastro['aposentadoria'] = cadastro['idade'] + (35 - (date.today().year - cadastro['contratação']))
print("=-" * 15, "***", "-=" * 15)
print(cadastro)
for k, v in cadastro.items():
    print(f"  - {k} tem o valor {v}")