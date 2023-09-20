valores = list()
for cont in range(0, 5):
    valores.append(int(input("Digite um numero: ")))
for posicao, item in enumerate(valores):
    print(f"Na posição {posicao} encontrei o valor {item}...")
print("Fim da lista.")

