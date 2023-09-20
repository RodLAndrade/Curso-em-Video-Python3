def leiaInt(msg):
    while True:
        try:              
            numeroint = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Digite um número inteiro!")
            continue
        except (KeyboardInterrupt):
            print("ERRO! O usuário preferiu nao digitar.")
            return 0
        else:
            return numeroint

def leiaFloat(msg):
    while True:
        try:              
            numerofloat = float(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Digite um número real!")
        except (KeyboardInterrupt):
            print("ERRO! O usuário preferiu nao digitar.")
            return 0
        else:
            return numerofloat

def executar_codigo():
    numi  = leiaInt('Digite um número inteiro: ')
    numf  = leiaFloat('Digite um número real: ')
    return f"O número inteiro digitado foi {numi} e o real foi {numf}."

print(executar_codigo())