reta1 = float(input("Digite o tamanho da primeira reta em centímetros: "))
reta2 = float(input("Digite o tamanho da segunda reta em centímetros: "))
reta3 = float(input("Digite o tamanho da terceira reta em centímetros: "))
c = reta1+reta2
b = reta1+reta3
a = reta2+reta3
if c > reta3 and b > reta2 and a > reta1:
    print("É um triangulo")
else:
    print("Não é um tringulo")