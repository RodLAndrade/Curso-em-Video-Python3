def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'Erro: {entrada} é um preço inválido!.')
        else:
            valido = True
            return float(entrada)
    
def validador_float(numero):
    try:
        return float(numero)
    except:
        return None
    
def loop_input_preços(msg):
    while True:
        numero = validador_float(input(msg).replace(',', '.'))
        if numero is None:
            print("ERRO! Digite um número!")
        else:
            break
    return(numero)