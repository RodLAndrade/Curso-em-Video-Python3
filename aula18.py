
#é possivel guardar listas dentro de listas ou "LISTAS COMPOSTAS"

individuo = []
perfil = []
maior = menor = 0
for c in range(0,3):
    individuo.append(str(input("Nome: ")))
    individuo.append(int(input("Idade: ")))
    perfil.append(individuo[:])
    individuo.clear()
for c in range(0,len(perfil)):
    print("-="*20,"-")
    print(f"Nome: {perfil[c][0]}\nIdade: {perfil[c][1]}")
for p in perfil:
    if p[1] > 21:
        print("-="*20,"-")
        print(f"{p[0]} é maior de idade")
        maior += 1
    else:
        print("-=" * 20, "-")
        print(f"{p[0]} é menor de idade")
        menor += 1
print("-=" * 20, "-")
print(f"Temos {maior} maiores de idade e {menor} menores de idade.")
print("-="*20,"-")
print(perfil)
print("-="*20,"-")