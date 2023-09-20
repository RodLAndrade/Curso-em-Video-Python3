total = cont = 0
num = int(input("Digite um numero para adicionar ao total (999 para parar): "))
while num != 999:
    total += num
    print(f"Até agora o total digitado é {total}")
    cont += 1
    num = int(input("Digite um numero para adicionar ao total (999 para parar): "))
print(f"Voce digitou {cont} numeros e o total foi {total}\nFim")
