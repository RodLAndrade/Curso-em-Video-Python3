def aumentar(numero, porcentagem, formatar = False):
    if formatar:
        return moeda(numero + ((numero / 100) * porcentagem))
    else:
        return numero + ((numero / 100) * porcentagem)

def diminuir(numero, porcentagem, formatar = False):
    if formatar:
        return moeda(numero - ((numero / 100) * porcentagem))
    else:
        return numero - ((numero / 100) * porcentagem)

def dobro(numero, formatar = False):
    if formatar:
        return moeda(numero * 2)
    else:    
        return numero * 2

def metade(numero, formatar = False):
    if formatar:
        return moeda(numero / 2)
    else:    
        return numero / 2

def moeda(msg):
    return f"R${msg:.2f}"