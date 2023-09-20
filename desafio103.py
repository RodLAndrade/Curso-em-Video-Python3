def ficha(j = '<desconhecido>',g = 0):
    print(f"O jogador {j} fez {g} gol(s).")


jog = (input("Jogador: "))
gol = (input("Gols: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jog.strip() == '':
    ficha(g = gol)
else:
    ficha(jog, gol)