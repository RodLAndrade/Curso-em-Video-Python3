num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 == num2:
    print(f"Os dois numeros são iguais.")
elif num1 > num2:
    print(f"O primeiro valor '{num1}' é o maior e o segundo valor '{num2}' é o menor.")
elif num2 > num1:
    print(f"O segundo valor '{num2}' é o maior e o segundo valor '{num1}' é o menor. ")
else:
    print("Digita certo o caraio")