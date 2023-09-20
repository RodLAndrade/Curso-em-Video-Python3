historico = {}
marcados = []
historico['Jogador'] = str(input("Jogador: "))
partidas = int(input(f"Quantas partidas o {historico['Jogador']}: "))
for c in range(0, partidas):
    marcados.append(int(input(f"Quantos gols foram feitos na partida {c+1}: ")))
historico['Gols'] = marcados[:]
historico['Total'] = sum(marcados)
print(historico)
print("-=" * 15, ">> *** <<", "=-" * 15)
for k, v in historico.items():
    print(f"O campo {k} tem o valor {v}.")
print("-=" * 15, ">> *** <<", "=-" * 15)
print(F"O jogador {historico['Jogador']} jogou: ")
for c, i in enumerate(historico['Gols']):
    print(f"  => Na partida {c+1}, fez {i} gols.")
print(f"Foi um total de {historico['Total']} gols.")
