lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))
c = lado1 + lado2
b = lado1 + lado3
a = lado2 + lado3
if a > lado1 and b > lado2 and c > lado3:
    if lado1 == lado2 and lado1 == lado3:
        print("É um triangulo equilatero!")
    elif lado1 != lado2 != lado3 != lado1:
        print("É um triangulo escaleno!")
    else:
        print("É um triangulo isosceles!")
else:
    print("Não é um triangulo!")
