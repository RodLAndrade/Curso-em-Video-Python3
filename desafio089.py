arquivo = []
boletim = []
while True:
    boletim.append(str(input("Nome do aluno: ")))
    boletim.append(float(input("Nota1: ")))
    boletim.append(float(input("Nota2: ")))
    arquivo.append(boletim[:])
    boletim.clear()
    continuar = str(input("Continuar?[S/N] ")).upper().strip()
    if continuar == "N":
        break
print("{:*^30}".format((">> BOLETINS <<")))
print("{:<5}".format("Nº"),end="")
print("{:<20}".format("Nome"),end="")
print("{:>5}".format("Média"))
print("*" * 30)
for count, item in enumerate(arquivo):
    print("{:<5}".format(f"{count + 1}"), end="")
    print("{:<20}".format(f"{item[0]}"), end="")
    print("{:<5}".format(f"{(item[1]+item[2])/2:.1f}"))
print("*" * 75)
while True:
    notas = int(input("Digite o número do aluno que deseja ver as notas, 999 para interromper: "))
    if notas == 999:
        break
    for c in range(0, len(arquivo)):
        if c == notas - 1:
            print(f"Notas de {arquivo[c][0]}: {arquivo[c][1], arquivo[c][2]}.")
            print("*" * 75)
print("{:*^75}".format((" >> FIM << ")))