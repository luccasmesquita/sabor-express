import os

restaurantes = ['Pizza', 'Sushi' ]

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

def opcao_invalida():
    print('Opção invalida!\n')
    input('Pressione "enter" para voltar ao menu principal!')
    main()

def cadastrar_novo_restaurante():
    os.system('clear')
    print('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('\nPressione "enter" para voltar ao menu principal!')
    main()

def listar_restaurantes():
    os.system('clear')
    print('Listando os restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}') 

    input('\nPressione "enter" para voltar ao menu principal!')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else :
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()