def separador():
    print('~' * 70)
    
def titulo(msg):
    separador()
    print(f'{msg}'.center(70))
    separador()

def validador_int(numero):
    try:
        return int(numero)
    except:
        return None

def loop_input_idade():
    while True:
        numero = validador_int(input("Idade: ").strip())
        if numero is not None:
            return numero
        else:
            print("ERRO! Digite uma idade válida!")
    
def input_nomes():
    return str(input("Nome: "))

def loop_input_opcao():
    while True:
        numero = validador_int(input("O que gostaria de fazer? ").strip())
        separador()
        if numero is not None and 0 > numero < 4:
            return numero
        else:
            print("ERRO! Digite uma opção válida!")
            separador()

def menu_principal():
    titulo("MENU PRINCIPAL")
    print(' 1 - Ver usuários cadastrados')
    print(' 2 - Cadastrar novo usuário')
    print(' 3 - Sair')
    separador()
    
def menu_1_ver_usuarios(cadastros):
    if cadastros:
        titulo("USUÁRIOS CADASTRADOS")
        for c, v in cadastros.items():
            print(f" {c}".ljust(50), end='')
            print(f"{v} anos ".rjust(20))
    else:
        print("Ainda não existem cadastros em nosso arquivos, faça o primeiro!")

def menu_2_cadastrar_usuario(cadastros):
    nome = (input_nomes())
    cadastros[nome] = (loop_input_idade())
    separador()

def executar()
    cadastros = {} 
    while True:
        menu_principal()
        opcao = loop_input_opcao() 
        if opcao == 1:
            menu_1_ver_usuarios(cadastros)
        elif opcao == 2:
            menu_2_cadastrar_usuario(cadastros)
        elif opcao == 3:
            break
    print("Até logo!".center(70))
    separador()
    return cadastros

executar()