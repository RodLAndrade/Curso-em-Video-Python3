n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))
if n1 > n2 > n3:
    print(f"O maior é {n1} e o menor é {n3}")
elif n1 > n3 > n2:
    print(f"O maior é {n1} e o menor é {n2}")
elif n2 > n1 > n3:
    print(f"O maior é {n2} e o menor é {n3}")
elif n2 > n3 > n1:
    print(f"O maior é {n2} e o menor é {n1}")
elif n3 > n1 > n2:
    print(f"O maior é {n3} e o menor é {n2}")
else:
    print(f"O maior é {n3} e o menor é {n1}")