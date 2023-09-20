preco = float(input("Digite o valor do produto: "))
pagamento = str(input("Digite a forma de pagamento, sendo (1)A vista dinheiro/cheque, (2)A vista no cartão, (3)Em até 2x no cartão e (4)3x ou mais no cartão.  "))
if pagamento == "1":
    print(f"O valor terá 10% de desconto! O preço final será R${preco-((preco/100)*10):.2f}.")
elif pagamento == "2":
    print(f"O valor terá 5% de desconto! O preço final será R${preco-((preco/100)*5):.2f}.")
elif pagamento == "3":
    print(f"O valor será o mesmo.")
elif pagamento == "4":
    print(f"O valor terá 20% de juros, o preço final será R${preco+((preco/100)*20):.2f}.")
else:
    print(f"Digita certo caraio.")
