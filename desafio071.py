print(f"{'*'*20}")
print("{:^20}".format("WELKOME TO KBANK"))
print(f"{'*'*20}")
saque = int(input("Digite o valor a ser sacado: R$"))
print(f"{'*'*20}")
nota1 = nota10 = nota20 = nota50 = 0
while True:
    if saque >= 50:
        saque -= 50
        nota50 += 1
    if saque < 50 and saque >= 20:
        saque -= 20
        nota20 += 1
    if saque < 20 and saque >= 10:
        saque -= 10
        nota10 += 1
    if saque < 10 and saque >= 1:
        saque -= 1
        nota1 += 1
    if saque == 0:
        break
print("O total de cédulas recebidas será:")
if nota50 > 0:
    print(f"{nota50} notas de R$50,00")
if nota20 > 0:
    print(f"{nota20} notas de R$20,00")
if nota10 > 0:
    print(f"{nota10} notas de R$10,00")
if nota1 > 0:
    print(f"{nota1} notas de R$1,00")
print(f"{'*'*20}")
print("{:^20}".format("FIM"))
print(f"{'*'*20}")

