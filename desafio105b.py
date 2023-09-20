def validador_float(numero):
    try:
        return float(numero.strip().replace(',', '.'))
    except:
        return None

def loop_input_numeros_float():
    while True:
        numero = validador_float(input("Digite um número: "))
        if numero is not None:
            print(f"Você digitou o número {numero}")
            return(numero)
        else:
            print("ERRO! Digite um número!")
 
def loop_continuar():
    while True:
        continuar = input("Continuar?(S/N) ").upper().strip()
        if len(continuar) == 1 and continuar in "SN":
            if continuar == "N":
                return False
            else:
                return True
        else:
            print("ERRO! Digite S ou N.")
            
def loop_situacao():
    while True:
        situacao = input("Deseja mostrar a situacao do aluno?(S/N) ").upper().strip()
        if len(situacao) == 1 and situacao in "SN":
            if situacao == "N":
                return False
            else:
                return True
        else:
            print("ERRO! Digite S ou N.")
            
def calcular_maior(numeros):
    return max(numeros)

def calcular_menor(numeros):
    return min(numeros)

def calcular_total(numeros):
    return len(numeros) 

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_situação(media):
    if media < 5:
        return "Ruim"
    if 5 <= media < 8:
        return "Medio"
    else:
        return "Bom"
    
def criar_resumo(numeros, situacao):
    resumo = {}
    resumo['Total'] = calcular_total(numeros)
    resumo['Maior'] = calcular_maior(numeros)
    resumo['Menor'] = calcular_menor(numeros)
    resumo['Média'] = calcular_media(numeros)
    if situacao:
        resumo['Situação'] = calcular_situação(resumo['Média'])
    return resumo

def executar_codigo():
    numeros = []
    while True:
        numeros.append(loop_input_numeros_float())
        if not loop_continuar():
            break
    if loop_situacao():
        return criar_resumo(numeros, True), "***"
    else:
        return criar_resumo(numeros, False), "---"
    
print(executar_codigo())