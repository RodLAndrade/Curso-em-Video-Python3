expressao = str(input("Digite a expressao matematica: "))
pilha = []
for simbolo in expressao:
    if simbolo == "(":
        pilha.append(simbolo)
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            break
if len(pilha) == 0:
    print("A expressão é válida!")
else:
    print("A expressão está errada :/")
