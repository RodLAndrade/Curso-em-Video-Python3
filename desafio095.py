historico = {}
arquivo = []
marcados = []
while True:
    historico['Jogador'] = str(input("Jogador: "))
    partidas = int(input(f"Quantas partidas {historico['Jogador']} jogou? "))
    for c in range(0, partidas):
        marcados.append(int(input(f"Quantos gols foram feitos na partida {c+1}: ")))
    historico['Gols'] = marcados[:]
    historico['Total'] = sum(marcados)
    arquivo.append(historico.copy())
    historico.clear()
    marcados.clear()
    continuar = str(input("Continuar?(S/N) ")).upper().strip()
    if continuar == "N":
         break
print("{:*^75}".format((">> HISTORICO <<")))
print("{:<5}".format("Nº"),end="")
print("{:<25}".format("Nome"),end="")
print("{:<40}".format("Média"),end="")
print("{:>5}".format("Total"))
print("*" * 75)
for count, item in enumerate(arquivo):
    print("{:<5}".format(f"{count + 1}"), end="")
    print("{:<25}".format(f"{item['Jogador']}"), end="")
    print("{:<40}".format(f"{item['Gols']}"), end="")
    print("{:>5}".format(f"{item['Total']}"), end="")
    print()
print("*" * 75)
while True:
    num = int(input("Mostrar dados de qual jogador?(999 para interromper)  "))
    if num == 999:
        break
    if num > len(arquivo):
        print("ERRO! Tente novamente.")
    for c in range(0, len(arquivo)):
        if c == num - 1:
            print(f"Levantamento jogador {arquivo[c]['Jogador']}: ")
            for u, i in enumerate(arquivo[c]['Gols']):
                print(f"  => Na partida {u+1}, fez {i} gols.")
    print("*" * 75)
print("*" * 31, "<< FIM >>", "*" * 31)

