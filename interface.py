#from bdinit import create_table, inserir_cliente, alterar_cliente, pesquisar_nome, remover_cliente, listar_todos, exibir_um, conexao
from bdinit import *
#create_table()

def menu():
    opcaoescolhida = int(input("\n Escolha uma nova opcao!  \n Menu:\n 1. Inserir Cliente\n 2. Alterar Cliente \n 3. Pesquisar por nome \n 4. Remover cliente \n 5. Listar todos \n 6. Exibir um \n 7. Sair\n  Insira uma opção: "))
    return(opcaoescolhida)

print("\n BOAS VINDAS A LOJA DE ROUPAS")
#opcao = int(input("\n Menu:\n 1. Cadastro\n 2. Alterar Cliente \n 3. Pesquisar por nome \n 4. Remover cliente \n 5. Listar todos \n 6. Exibir um \n 7. Sair\n  Insira uma opção: "))
opcao = int(input("\n Menu:\n 1. Cadastro Cliente\n 2. Login Cliente \n 3. Ver Itens da Loja \n 4. Login Funcionário \n 5. Sair\n  Insira uma opção: "))
# Login Funcionario sem cadastro pois a loja vai começar com pelo menos um gerente, e ele que vai cadastrando os funcionarios
while True:
    if (opcao == 1):
        print("\n CADASTRO \n")
        nome = input("Insira o nome do cliente: ")
        user = input("Insira o usuario do cliente: ")
        senha = input("Insira a senha do cliente: ")
        email = input("Insira o email do cliente: ")
        cpf = input("Insira o cpf do cliente: ")
        is_flamengo = input("Digite se você torce para o flamengo (True/False): ")
        is_op = input("Digite se você assiste One Piece (True/False): ")
        is_souza = input("Digite se você é de souza (True/False): ")
        VALUES = [nome, user, senha, email, cpf, is_flamengo, is_op, is_souza]
        print(VALUES)
        inserir_cliente(VALUES)
        print("Cliente cadastrado com sucesso")
        opcao = 0
    elif (opcao == 2):
        print("\n LOGIN \n")
        user = input("Insira o usuario do cliente: ")
        senha = input("Insira a senha do cliente: ")
        info_cliente = login_cliente(user, senha)
        if info_cliente != False:
            print("\n Login Feito com sucesso \n")
            # agora está logado -> pode fazer pedidos
            pass
        else:
            print("\n Informações incorretas \n")
    elif (opcao == 3):
        print("\n Itens da Loja: \n")

    elif (opcao == 4):
        print("\n LOGIN FUNCIONÁRIO: \n")
        email = input("Insira seu email: ")
        senha = input("Insira seu senha: ")
        id_func = login_funcionario(email,senha)
        if id_func != False:
            print("\n Login do funcionario feito com sucesso \n")
            if check_info('cod_func', id_func, 'cod_func', 'gerente') != False: # não está dando certo aqui, sempre vai dar False
                interface_gerente(id_func)
            else:
                interface_vendedor(id_func)
        else:
            print("\n Informações incorretas \n")
    elif (opcao == 5):
        print("Obrigada por usar nosso sistema\n\n")
        conexao.close()
        break

    elif (opcao < 0) or (opcao > 7):
        print("Essa opcao não existe, selecione outra")
        opcao = 0
        continue
    else:
        prox = input("\n Digite qualquer digito para continuar: ")
        opcao = menu()

exit

"""
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
"""