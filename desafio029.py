print("Vamos descobrir se você vai tomar uma multa.")
velocidade = int(input("Qual a velocidade maxima que você dirigiu? "))
if velocidade > 80:
    multa = (velocidade-80)*7.00
    print(f"Você foi multado! O valor da multa será R${multa:.2f}\nBem feito, fica esperto seu otário.")
else:
    print("Você não foi multado!\nNão fez mais que sua obrigação.\n\nOtário.")

