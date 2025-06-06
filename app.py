import os
print("""
Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
      """)

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('2. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))

def finalizar_app():
    os.system('clear')
    # os.system('cls') / no windowns
    print('Finalizando o app\n')

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