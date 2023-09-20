def fatorial(num, show=False):
    """Faz o fatorial do número "num"

    Args:
        num (int)       : número que será fatorado
        show (Opcional) : mostra ou não a conta do fatorial

    Returns:
        fat: o resultado da fatoração de "num"
    
    Função criada pela sua mãe."""

    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        fat *= c
    return fat

print(fatorial(5, show=True))
help(fatorial)