num = int(input("Digite um numero para ser convertido: "))
tipo = int(input("Qual a base para conversao? (1)Binário (2)Octodecimal (3)Hexadecimal: "))
if tipo == 1:
    print(f"O numero {num} corresponde a {bin(num)[2:]} em Binário.")
elif tipo == 2:
    print(f"O numero {num} corresponde a {oct(num)[2:]} em Octodecimal.")
elif tipo == 3:
    print(f"O numero {num} corresponde a {hex(num)[2:]} em Hexadecimal.")
else:
    print("Digita certo o caraio.")