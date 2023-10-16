from bdinit import create_table, inserir_cliente, alterar_cliente, pesquisar_nome, remover_cliente, listar_todos, exibir_um, conexao

#create_table()

def menu():
    opcaoescolhida = int(input("\n Escolha uma nova opcao!  \n Menu:\n 1. Inserir Cliente\n 2. Alterar Cliente \n 3. Pesquisar por nome \n 4. Remover cliente \n 5. Listar todos \n 6. Exibir um \n 7. Sair\n  Insira uma opção: "))
    return(opcaoescolhida)

print("\n BOAS VINDAS A LOJA DE ROUPAS")
opcao = int(input("\n Menu:\n 1. Inserir Cliente\n 2. Alterar Cliente \n 3. Pesquisar por nome \n 4. Remover cliente \n 5. Listar todos \n 6. Exibir um \n 7. Sair\n  Insira uma opção: "))

while True:
    if (opcao == 1):
        print("\n INSERIR CLIENTE \n")
        nome = input("Insira o nome do cliente: ")
        user = input("Insira o usuario do cliente: ")
        senha = input("Insira a senha do cliente: ")
        email = input("Insira o email do cliente: ")
        cpf = input("Insira o cpf do cliente: ")
        VALUES = [nome, user, senha, email, cpf]
        print(VALUES)
        inserir_cliente(VALUES)
        print("Cliente cadastrado com sucesso")
        opcao = 0

    elif (opcao == 2):
        print("\n ALTERAR CLIENTE \n")
        chave = input("Insira o usuario do cliente: ")
        coluna = input("Insira qual informação quer mudar do cliente (nome, email...): ")
        novo = input("Insira a nova informação do cliente: ")
        
        alterar_cliente(coluna, novo, chave)

        print("Cliente atualizado com Sucesso")
        opcao = 0

    elif (opcao == 3):
        print("\n PESQUISAR POR NOME \n")
        name = input("Insira o nome do cliente: ")
        retorno = pesquisar_nome(name)
        if len(retorno) == 0:
            print("Esse cliente não existe. Cheque a gramática ou insira um cliente novo.")

        opcao = 0

    
    elif (opcao == 4):
        print("\n REMOVER CLIENTE \n")
        chave = input("Insira o usuario do cliente: ")
        
        retorno = exibir_um(chave)
        if len(retorno) > 0:
            remover_cliente(chave)
            print("Cliente apagado com Sucesso")
        else:
            print("Esse cliente não existe. Cheque a gramática.")

        opcao = 0
    
    elif (opcao == 5):
        print("\n LISTAR TODOS \n")
        
        lista = listar_todos()
        for pessoa in lista:
            print(pessoa)

        opcao = 0
    
    elif (opcao == 6):
        print("\n EXIBIR UM \n")
        chave = input("Insira o usuario do cliente: ")
        retorno = exibir_um(chave)
        if len(retorno) == 0:
            print("Esse cliente não existe. Cheque a gramática ou insira um cliente novo.")

        opcao = 0

    elif (opcao == 7):
        print("Obrigada por usar nosso sistema\n\n")
        conexao.close()
        break

    if (opcao < 0) or (opcao > 7):
        print("Essa opcao não existe, selecione outra")
        opcao = 0
        continue

    else:
        prox = input("\n Digite qualquer digito para continuar: ")
        opcao = menu()

exit