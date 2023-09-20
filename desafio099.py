from time import sleep
lista = []

def separador():
    print("-=" * 8, " >> *** << ", "=-" * 8)

def maior(* valores):
    mai = 0
    count = 0
    for c, v in enumerate(valores):
        if c == 0 or v > mai:
            mai = v
        count += 1
    if mai == 0:
        print("Não foi informado nenhum número, lista ta vazia :/")
    else:
        for c, v in enumerate(valores):
            print(f"{v} ", end='', flush=True)
            sleep(0.5)
        print(f"\nForam informados {count} números, o maior é: {mai}")


while True:
    num = ""
    while num not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999): 
        num = int(input("Digite um numero de 0 a 9, 999 para encerrar: "))
    if num == 999:
        break
    lista.append(num)

separador()   
maior(* lista)
separador()