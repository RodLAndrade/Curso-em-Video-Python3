def aumentar(numero = 0, porcentagem = 0, formatar = False):
    resp = numero + ((numero / 100) * porcentagem)
    if formatar:
        return moeda(resp)
    else:
        return resp

def diminuir(numero = 0, porcentagem = 0, formatar = False):
    resp = numero - ((numero / 100) * porcentagem)
    if formatar:
        return moeda(resp)
    else:
        return resp

def dobro(numero = 0, formatar = False):
    resp = numero * 2
    if formatar:
        return moeda(resp)
    else:    
        return resp

def metade(numero = 0, formatar = False):
    resp = numero / 2
    if formatar:
        return moeda(resp)
    else:
        return resp

def moeda(numero = 0, moeda = 'R$'): 
    return f"{moeda}{numero:>.2f}".replace('.', ',')

def resumo(numero = 0, aumento = 10, reducao = 5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(numero)}")
    print(f"Metade do  preço: \t{metade(numero, True)}.")
    print(f"Dobro do preço: \t{dobro(numero, True)}.")
    print(f"Aumento de {aumento}%: \t{aumentar(numero, 10, True)}.")
    print(f"Redução de {reducao}%:  \t{diminuir(numero, 13, True)}.")
    print("-" * 30)

