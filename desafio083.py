listaexpressao = []
aberto = []
fechado = []
expressao = str(input("Digite uma expressão matemática: ")).strip()
for count, item in enumerate(expressao):
    listaexpressao.append(item)
for count, item in enumerate(listaexpressao):
    if item in "()":
        if item == "(":
            aberto.append(item)
        else:
            fechado.append(item)
if len(aberto) == len(fechado):
    print("É uma expressão válida!")
else:
    print("É uma expressão inválida :/")

