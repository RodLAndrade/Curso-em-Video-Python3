def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print("ERRO! Digite um núemro inteiro válido.")
        if ok:
            break
    return valor

num = leiaInt('Digite um número inteiro: ')
print(f"Você acabou de digitar o número {num}.")