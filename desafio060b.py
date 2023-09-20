num = int(input("Digite um numero: "))
mult = num * (num - 1)
num += -1
for c in range(1, num-1):
    mult += mult * c
print(f"O total da fatoração é {mult}")