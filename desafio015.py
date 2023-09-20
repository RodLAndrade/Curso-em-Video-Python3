d = int(input('Digite a quantidade de dias que ficou com o carro: '))
k = int(input('Digite a quantidade de kilometros rodados: '))
t = (d*60)+(0.15*k)
print(f'Voce ficou com o carro por {d} dias e rodou {k}km, o valor total da locação é R${t:.2f}.')
