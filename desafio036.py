print("\033[1;97mCalculadora de emprestimos\033[m")
valor = float(input("Digite o valor da casa que deseja comprar: R$"))
anos = int(input("Em quantos anos deseja pagar o imóvel: "))
salario = float(input("Digite o valor de sua renda mensal: R$"))
parcela = valor/(anos*12)
porcentagem = (salario / 100) * 30
print(f"Valor maximo de parcela comportado: R${porcentagem}\nParcela: R${parcela:.2f}")
if parcela > porcentagem:
    print("Desculpe, mas a parcela fica maior que comportado por seu salario.")
else:
    print("Parabéns, o empréstimo foi aprovado!")  