print("-----Calculadora de multa------")
velocidade = int(input("Qual a velocidade máxima que você atingiu? "))
print(f"Você foi multado, o valor da multa será R${(velocidade - 80)*7:.2f}! Otário." if velocidade > 80 else "Você não foi multado, não fez mais que a sua obrigação.\nOtário.")
print("-----------FIM-----------")