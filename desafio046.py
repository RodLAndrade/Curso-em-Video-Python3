from time import sleep
inic = str(input("Digite '0' para começar a contagem regressiva! "))
if inic == "0":
    print("Iniciando a contagem...")
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print("MUITO LOUCO")
else:
    print("Digite certo caraio")