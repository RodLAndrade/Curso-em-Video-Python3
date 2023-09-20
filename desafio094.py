pessoa = {}
cadastro = []
soma = 0
while True:
    pessoa['Nome'] = str(input("Nome: "))
    while True:
        pessoa['Sexo'] = str(input("Sexo:(M/F) ")).upper().strip()
        if pessoa['Sexo'] in 'MF':
            break
    pessoa['Idade'] = int(input("Idade: "))
    soma += pessoa['Idade']
    cadastro.append(pessoa.copy())
    pessoa.clear()
    while True:
        continuar = str(input("Pressione qualquer botão para continuar, 'N' para parar: ")).upper().strip()
        if continuar in "SN":
            break
    if continuar == "N":
        break
media = soma / len(cadastro)
print(f"O Total de pessoas cadastradas foram {len(cadastro)}")
print(f"A média de idade é {media}.")
print("As mulheres cadastradas são: ",end='')
for p in cadastro:
    if p['Sexo'] == 'F':
        print(f"{p['Nome']}.. ",end='')
print("\nAs pessoas com idade acima da média são: ")
for i in cadastro:
    if i['Idade'] > media:
        for k, v in i.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<< FIM >>")