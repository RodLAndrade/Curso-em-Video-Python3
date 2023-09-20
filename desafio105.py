arquivos = dict()
Nota = list()
def notas(*num, sit=False):
    """_summary_
    Args:
        sit (bool, optional): indica se deve ou não indicar a situação.
        num (float): uma ou mais notas do aluno (aceita varias).
    Returns:
        arquivo: dicionario com varias informações sobre a situação da turma.
    Função criada pela sua mãe.
    """
    global continuar
    valor = soma = media = 0
    ok = False
    while True:
      #validador  
        while True:
            ok = False
            nume = str(input(num))
            if nume.isnumeric():
                valor = float(nume)
                ok = True
                Nota.append(valor)
            else:
                print("ERRO! Digite um numero inteiro.")
            if ok:
                print(f"Você acabou de digitar o número {nume}")
                break

    
        continuar = str(input("Continuar?(S/N) ")).upper().strip()
        if continuar == "N":
            break
    for c in range (0, len(Nota)):
        soma += Nota[c]
        media = soma / len(Nota)
    arquivo['Total'] = len(Nota)
    arquivo['Maior'] = max(Nota)
    arquivo['Menor'] = min(Nota)
    arquivo['Media'] = media
    situacao = input("Deseja mostrar a situação do aluno?(S/N) ").upper()
    while situacao not in "SN":
        situacao = str(input("Digite 'S' ou 'N'! Deseja mostrar a situação do aluno?(S/N) ")).upper()
    if situacao in "Ss":
        sit = True   
    if sit == True:
        if media < 5:
            arquivo['Situação'] = str("Ruim") 
        elif 5 <= media < 7:
            arquivo['Situação'] = str("Média")
        else:
            arquivo['Situação'] = str("Boa")
    return Nota, arquivo

nume = notas("Digite um número: ")
if continuar == "N":
    print(Nota)
    print(arquivo)

    

    