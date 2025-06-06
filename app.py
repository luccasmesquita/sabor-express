print("""
Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
      """)

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('2. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))
print(f'Você escolheu a opção {opcao_escolhida}')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurante')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
elif opcao_escolhida == 4:
    print('Encerrando o programa')
else :
    print('Escolha uma opção valida')