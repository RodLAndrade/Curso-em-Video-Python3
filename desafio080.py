numbers = []
entradas = 0
while entradas <= 4:
    num = int(input("Digite um número: "))
    if num in numbers:
        print(f"O número duplicado, não foi possivel adicionar à lista.")
    else:
        if entradas == 0 or num > numbers[-1]:
            numbers.append(num)
            entradas += 1
            print(f"O número {num} foi adicionado com sucesso ao final da lista.")
        else:
            count = 0
            while count < len(numbers):
                if num <  numbers[count]:
                    numbers.insert(count, num)
                    entradas += 1
                    print(f"O número {num} foi adicionado com sucesso na posição {count}.")
                    break
                count += 1
print(numbers)