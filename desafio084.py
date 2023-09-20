cadastros = []
pessoa = []
pesado = leve = 0
while True:
    pessoa.append(str(input("Digite o nome: ")))
    pessoa.append(float(input("Digite o peso: ")))
    cadastros.append(pessoa[:])
    pessoa.clear()
    continuar = str(input("Digite 'N' para encerrar, qualquer coisa para continuar: ")).upper().strip()
    if continuar == "N":
        break
for count, item in enumerate(cadastros):
    if count == 0 or pesado <= item[1]:
        pesado = item[1]
    if count == 0 or leve >= item[1]:
        leve = item[1]
print("-" * 20)
print(f"No total foram cadastradas {len(cadastros)} pessoas.")
print(f"Os mais pesados são: ",end="")
for item in cadastros:
    if item[1] == pesado:
        print(f"{item[0]}.. ",end="")
print(f"\nOs mais leves são: ",end="")
for item in cadastros:
    if item[1] == leve:
        print(f"{item[0]}.. ",end="")
print("\nFIM")