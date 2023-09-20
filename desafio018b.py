from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O seno é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}.')