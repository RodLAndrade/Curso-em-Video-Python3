nome = str(input("Digite seu nome: "))
separado = nome.split()
rev = list(reversed(separado))
print(f"{nome}\nprimeiro nome: {separado[0]}\nultimo nome: {rev[0]}")
