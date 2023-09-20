print(f"{'='*20}\nSenso da URSAL\n{'='*20}")
maiordeidade = homens = mulhermenorde20 = 0

while True:
    print("Cadastre um camarada! ")
    idade = int(input("Digite a idade: "))
    sexo = ""
    while sexo != "M" and sexo != "F":
        sexo = str(input("Qual o sexo?(M/F) ")).upper().strip()
    if sexo == "M":
        homens += 1
    if idade > 18:
        maiordeidade += 1
    if sexo == "F" and idade < 20:
        mulhermenorde20 += 1
    print(f"{'='*20}")
    continuar = ""
    while continuar != "S" and continuar != "N":
        continuar = str(input("Quer continuar?(S/N)")).upper().strip()
        print(f"{'='*20}")
    if continuar == "N":
        break
print(f"Maiores de 18 anos: {maiordeidade}")
print(f"Homens: {homens}")
print(f"Mulheres com menos de 20 anos: {mulhermenorde20}\n{'='*20}\nFIM\n{'='*20}")

