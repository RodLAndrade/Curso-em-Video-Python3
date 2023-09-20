from math import sqrt, pow
o = float(input('Digite o comprimento do cateto oposto: '))
a = float(input('Digite o comprimento do cateto adjacente: '))
print(f'A hipotenusa é {sqrt((pow(o,2))+(pow(a,2))):.2f}.')