import os

def exibir_nome_do_programa():
    print("""
    Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
        """)
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('2. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('clear')
    # os.system('cls') / no windowns
    print('Finalizando o app\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    elif opcao_escolhida == 4:
        finalizar_app()
    else :
        print('Escolha uma opção valida')

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()