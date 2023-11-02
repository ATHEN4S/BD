#from bdinit import create_table, inserir_cliente, alterar_cliente, pesquisar_nome, remover_cliente, listar_todos, exibir_um, conexao, login_cliente login_funcionario
from bdinit import *

#create_table()

print("\n BOAS VINDAS A LOJA DE ROUPAS")

#opcao = int(input("\n Menu:\n 1. Cadastro Cliente\n 2. Login Cliente \n 3. Ver Itens da Loja \n 4. Login Funcionário \n 5. Sair\n  Insira uma opção: "))
# Login Funcionario sem cadastro pois a loja vai começar com pelo menos um gerente, e ele que vai cadastrando os funcionarios
LOG = 0
ID = 0
opcao = int(input("\n 1.LOGIN\n 2.CADASTRO\n 3.VER ITENS\n  4. FECHAR \n Insira uma opção: "))
while True:
    if (opcao == 1):
        # LOGINS SEPARADOS EM CLIENTE E FUNCIONARIOS
        tipo = int(input("\n LOGIN: \n 1. Login como cliente\n 2. Login como funcionario"))

        if tipo == 1:
            #CLIENTE
            print("\n LOGIN \n")
            user = input("Insira o usuario do cliente: ")
            senha = input("Insira a senha do cliente: ")
            info_cliente = login_cliente(user, senha)
            if info_cliente != False:
                print("\n Login Feito com sucesso \n")
                ID = ID_cliente(user)
                LOG = 1
                # agora está logado -> pode fazer pedidos
                opcao == 0
                break
            else:
                print("\n Informações incorretas \n")

        elif tipo == 2:
            #FUNCIONARIO
            print("\n LOGIN FUNCIONÁRIO: \n")
            email = input("Insira seu email: ")
            senha = input("Insira seu senha: ")
            id_func = login_funcionario(email,senha)
            if id_func != False:
                print("\n Login do funcionario feito com sucesso \n")
                LOG = 2
                if check_info('cod_func', id_func, 'cod_func', 'gerente') != False: # não está dando certo aqui, sempre vai dar False
                    LOG = 3
                    interface_gerente(id_func)
                else:
                    interface_vendedor(id_func)
            else:
                print("\n Informações incorretas \n")
        else:
            print("Essa não é uma opcao válida. Tente novamente")
            continue

        opcao == 0


    elif(opcao == 2):
        #CADASTRO
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
        print("Cliente cadastrado com sucesso\n")
        opcao = 0

    elif(opcao == 3):
        #VER ITENS
        print("\nITENS NO CATÁLOGO\n")
        lista = listar_item()
        for item in lista:
            print(item)
    
        desconto()
        opcao == 0
        break

if LOG == 1:
    opcao = int(input("\n 1.PERFIL 2.VER ITENS\n 3.HISTÓRICO DE PEDIDOS\n  4. SAIR \n Insira uma opção: "))
    while True:
        if (opcao == 1):
            print("\n PERFIL \n")
            VALUES = [nome, user, senha, email, cpf, is_flamengo, is_op, is_souza]
            print(VALUES)
            inserir_cliente(VALUES)
            print("Cliente cadastrado com sucesso")
            opcao = 0
        elif (opcao == 2):
            print("\n ITENS DA LOJA: \n")
            continue
            
        elif (opcao == 3):
            print("\n HISTORICO DE PEDIDOS: \n")
            desconto()
            continue
            

        elif (opcao == 4):
            print("Obrigada por usar nosso sistema\n\n")
            
        elif (opcao < 0) or (opcao > 7):
            print("Essa opcao não existe, selecione outra")
            opcao = 0
            continue

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