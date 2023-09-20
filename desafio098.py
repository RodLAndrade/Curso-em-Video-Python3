from time import sleep
def separador():
    print("-=" * 8, " >> *** << ", "=-" * 8)


def contador(i, f, p):
    if p == 0:
        p = 1 
    if p < 0:
        p *= -1
        
    print(f"Contadem de {i} até {f} de {p} em {p}")

    if i > f:
        count = i
        while count >= f:
            print(f"{count} ", end="", flush=True)
            sleep(0.5)
            count -= p          
        print("Fim")
    else:    
        count = i
        while count <= f:
 
            print(f"{count} ", end="", flush=True)
            sleep(0.5)
            count += p           
        print("Fim")


separador()
contador(1, 10, 1)
separador()
contador(10, 0, 2)
separador()
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
separador()
contador(inicio, fim, passo)
separador()