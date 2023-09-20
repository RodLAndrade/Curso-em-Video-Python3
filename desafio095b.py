historico = {}
arquivo = []
marcados = []
while True:
    historico.clear()
    marcados.clear()
    historico['Jogador'] = str(input("Jogador: "))
    partidas = int(input(f"Quantas partidas {historico['Jogador']} jogou? "))
    for c in range(0, partidas):
        marcados.append(int(input(f"Quantos gols foram feitos na partida {c+1}: ")))
    historico['Gols'] = marcados[:]
    historico['Total'] = sum(marcados)
    arquivo.append(historico.copy())
    continuar = str(input("Continuar?(S/N) ")).upper().strip()
    if continuar == "N":
         break
print("{:*^65}".format((">> HISTORICO <<")))
print("{:<5}".format("Nº"),end="")
for i in historico.keys():
    print(f"{i:<20}",end="")
print()
print("*" * 65)
for count, item in enumerate(arquivo):
    print(f"{count + 1:<5}", end="")
    for d in item.values():
        print(f"{str(d):<20}", end="")
    print()
print("*" * 65)
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
