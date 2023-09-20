def somar(a = 0, b = 0, c = 0):
    """
    ->Faz a soma de tres valores e mostra o resultado na tela

    Args:
        a (int, optional): primeiro valor. Defaults to 0.
        b (int, optional): segundo valor. Defaults to 0.
        c (int, optional): terceiro valor. Defaults to 0.

        Função criada pela sua mãe.   
    """
    s = a + b + c
    return s

while True:
    a = int(input("Digite um numero: "))
    b = int(input("Digite o segundo numero: "))
    c = int(input("Digite o terceiro numero: "))
    somar(a, b, c)
    continuar = input("Continuar?(S/N) ").upper()
    if continuar == "N":
        break
print("FIM!")