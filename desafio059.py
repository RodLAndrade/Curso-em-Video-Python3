num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite um segundo numero inteiro: "))
opção = ""
soma = ""
mult = ""
while opção != 5:
    opção = int(input("-----\nO que deseja fazer com esses numeros?\n(1) Somar\n(2) Multiplicar\n(3) Ver qual é o maior\n(4) Novos numeros\n(5) Sair do programa\n-----\nDigite sua escolha: "))
    print("-----")
    if opção > 5:
        print("Digita certo caraio.")
    else:
        if opção == 1:
            soma = num1 + num2
            print(f"A soma dos numeros {num1} e {num2} é igual a {soma}.")
        elif opção == 2:
            mult = num1 * num2
            print(f"O produto dos numeros {num1} e {num2} é igual a {mult}.")
        elif opção == 3:
            if num1 > num2:
                print(f"O primeiro numero digitado, {num1}, é o maior.")
            elif num2 > num1:
                print(f"O segundo numero digitado, {num2}, é o maior.")
            else:
                print(f"Os dois numeros digitados são iguais. {num1} e {num2}.")
        elif opção == 4:
            num1 = int(input("Digite outros numeros.\nDigite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))
print("FIM\n-----")