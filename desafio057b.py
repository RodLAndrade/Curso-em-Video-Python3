sexo = str(input("Digite seu sexo(M/F): ")).strip().upper()
while sexo not in "FM":
    sexo = str(input("Digita certo caraio\nDigite seu sexo(M/F): ")).strip().upper()
print(f"Sexo {sexo} registrado com sucesso.\nFIM")