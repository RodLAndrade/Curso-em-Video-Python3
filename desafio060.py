num = int(input("Digite um numero: "))
total = ""
mult = num * (num - 1)
num += -2
while num > 0 :
    mult = mult * num
    num -= 1
print(f"\nO total é {mult}.")