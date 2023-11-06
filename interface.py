#from bdinit import create_table, inserir_cliente, alterar_cliente, pesquisar_nome, remover_cliente, listar_todos, exibir_um, conexao, login_cliente login_funcionario
from bdinit import *
#create_table()

print("\n BOAS VINDAS A LOJA DE ROUPAS")

#opcao = int(input("\n Menu:\n 1. Cadastro Cliente\n 2. Login Cliente \n 3. Ver Itens da Loja \n 4. Login Funcionário \n 5. Sair\n  Insira uma opção: "))
# Login Funcionario sem cadastro pois a loja vai começar com pelo menos um gerente, e ele que vai cadastrando os funcionarios
LOG = 0
ID = ""
tipo = 0

cliente = ["ID: ", "Username: ", "Senha: ", "Nome: ", "Email: ", "CPF: ", "Torcedor do Flamengo: ", "Fã de One Piece: ", "De Souza: "]
endereco = ["Cidade: ", "Estado: ", "Rua: ", "Numero: ", "CEP: "]

#INTERFACE USUARIOS
opcao = int(input("\n 1.LOGIN\n 2.CADASTRO\n 3.VER ITENS\n 4.FECHAR \n Insira uma opção:\n  > "))
login_realizado = False
while (opcao != 4 and tipo != 4) or (login_realizado != True):
    if opcao == 0:
        opcao = int(input("\n      MENU \n 1.LOGIN\n 2.CADASTRO\n 3.VER ITENS\n 4.FECHAR \n Insira uma opção:\n  > "))
    if (opcao == 1) and login_realizado != True:
        # LOGINS SEPARADOS EM CLIENTE E FUNCIONARIOS
        tipo = int(input("\n LOGIN: \n 1. Login como cliente\n 2. Login como funcionario \n 3. Voltar \n 4. Sair\n > "))

        if tipo == 1:
            #CLIENTE
            print("\n LOGIN \n")
            user = input("   Insira o usuario do cliente: ")
            senha = input("   Insira a senha do cliente: ")
            info_cliente = login_cliente(user, senha)
            print("--->", info_cliente)
            if info_cliente != False:
                print("\n Login Feito com sucesso! \n")
                ID = ID_cliente(user)
                LOG = 1
                # agora está logado -> pode fazer pedidos
                login_realizado = True
                break
            else:
                print("\n Informações incorretas \n")
                voltar = input("Digite qualquer caractere para voltar pro menu inicial, 1 para tentar novamente.\n >")
                if voltar == "1":
                    opcao = 1
                    tipo = 1
                    
                else:
                    opcao = 0
                    continue
            
        elif tipo == 2:
            #FUNCIONARIO
            print("\n LOGIN FUNCIONÁRIO: \n")
            email = input("   Insira seu email: ")
            senha = input("   Insira seu senha: ")
            id_func = login_funcionario(email,senha)
            if id_func != False:
                print("\n Login do funcionario feito com sucesso! \n")
                LOG = 2
                if check_info('funcFK', id_func, 'funcFK', 'gerente') != False:
                    LOG = 3
                    interface_gerente(id_func)
                else:
                    interface_vendedor(id_func)
                login_realizado = True
            else:
                print("\n Informações incorretas \n")
        
        elif tipo == 3:
            opcao = 0
        
        elif tipo == 4:
            quit()

    elif(opcao == 2):
        #CADASTRO
        print("\n CADASTRO \n")
        nome = input("  Insira o nome do cliente: ")
        user = input("  Insira o usuario do cliente: ")
        senha = input("  Insira a senha do cliente: ")
        email = input("  Insira o email do cliente: ")
        cpf = input("  Insira o cpf do cliente: ")
        is_flamengo = input("  Torce para o flamengo (True/False)?\n > ")
        is_op = input("  Assiste One Piece (True/False)?\n > ")
        is_souza = input("  É de souza (True/False)?\n > ")
        VALUES = [nome, user, senha, email, cpf, is_flamengo, is_op, is_souza]
        print(VALUES)
        inserir_cliente(VALUES)
        print("Cliente cadastrado com sucesso!\n")
        opcao = 0

    elif(opcao == 3):
        #VER ITENS
        #verificar produtos por nome, faixa de preço, categoria e se foram fabricados em Mari
        cont = 0
        print("\nITENS NO CATÁLOGO\n")
        lista = listar_item()
        
        for item in lista:
            cont += 1
            print(cont,". ",item)
        
        filtrar_item_input = input("Deseja filtrar os itens disponíveis? (S/N) > ")
        if filtrar_item_input.upper() == 'S':
            filtrar_itens()
        else:
            opcao = 0
    
    elif (opcao == 4):
        print("\n Volte Sempre !\n\n")
        break
    
    elif login_realizado == True:
        break

    else:
        print("Essa opcao não existe, selecione outra\n")
        opcao = int(input("  > "))
        continue


#INTERFACE CLIENTES
if LOG == 1:
    opcao = int(input("\n BEM VINDOS A LOJA ATH3NAS! \n 1.PERFIL\n 2.VER ITENS\n 3.HISTÓRICO DE PEDIDOS\n 4.CARRINHO\n 5. SAIR\n   Insira uma opção: "))
    while True:
        if (opcao == 0):
            opcao = int(input("\n MENU PRINCIPAL \n 1.PERFIL\n 2.VER ITENS\n 3.HISTÓRICO DE PEDIDOS\n 4.CARRINHO\n 5. SAIR\n   Insira uma opção: "))
            continue
        elif (opcao == 1):
            print("\nPERFIL\n")
            lista = ver_perfil(ID)
            
            #Visualizar Perfil
            for i in range(len(cliente)-1):
                print(cliente[i], lista[i])

            #Visualizar Endereço - se não tiver, opção de adicionar um.
            if checar_endereco(ID) == False:
                ck = input("Você ainda não adicionou endereço de entrega. Deseja adicionar? (s/n)\n >")
                if (ck == "s") or (ck == "S"):
                    adicionar_endereco(ID)
            else:
                listaEND = ver_end(ID)
                for i in range(len(endereco)):
                    print(endereco[i], listaEND[i])
            continuar = input("Digite qualquer coisa para prosseguir.\n >")
            opcao = 0
            continue
        
        # Ver itens da loja para possivelmente add ao carrinho
        elif (opcao == 2):
            print("\n ITENS DA LOJA: \n")
            lista = listar_item()
            while True:
                for item in lista:
                    print(item)

                filtrar_itens1 = input("Deseja filtrar os itens disponíveis? (S/N) > ")
                if filtrar_itens1.upper() == 'S':
                    filtrar_itens()
                try:
                    add_aocarrinho = int(input("\n Digite o ID(INTEIRO) do item que deseja adicionar ao carrinho: \n -----> "))
                except ValueError:
                    print("\n -----------ERRO: NÃO FOI DIGITADO UM NÚMERO INTEIRO----------\n ")
                is_item = check_info('item_id', add_aocarrinho, 'item_id', 'item')
                if is_item != False:
                    qtd_item = 0
                    no_estoque = estoque_item_especifico(is_item) # Quantidade desse item específico no estoque
                    while qtd_item < 1 or qtd_item > no_estoque:
                        qtd_item = int(input("\nDigite a quantidade do item que deseja adicionar ao carrinho\n-------> "))
                        if qtd_item > no_estoque:
                            print("---- Não existe essa quantidade de itens no estoque, tente novamente... ----\n")
                    inserir_item_carrinho(ID, is_item, qtd_item)
                else:
                    print("Item ID inválido")
                print(" -------- CARRINHO DE COMPRAS ------------")
                listar_carrinho(ID)
                ask = input("\nDigite se você deseja continuar (s/n):\n ----> ")
                ask = ask.upper()
                while ask != 'S' and ask != 'N':
                    ask = input("\nDigite se você deseja continuar (s/n):\n ----> ")
                    ask = ask.upper()
                if ask == 'N':
                    break
            
        elif (opcao == 3):
            print("\n HISTORICO DE PEDIDOS: \n")
            itens = "ID do pedido | Quantidade de itens | Valor total "
            historico = verHistorico(ID)
            print(itens)
            for a in historico:
                print(a)
            input("\nDigite qualquer caractere para voltar:\n ----> ")
            opcao = 0
        
        elif (opcao == 4):
            interface_carrinho(ID)
            opcao = 0
            continue

        elif (opcao == 5):
            print("\nObrigada por usar nosso sistema. Volte sempre!\n")
            break
            
        elif (opcao < 0) or (opcao > 5):
            print("Essa opcao não existe, selecione outra\n")
            opcao = int(input("  > "))
            continue

        opcao = 0


#INTERFACE GERENTE
if LOG == 3:
    opcao = int(input("\n MENU - GERENTE \n 1. ESTOQUE \n 2. VER VENDEDORES DO SETOR\n 3. RELATORIO MENSAL\n 4. ADICIONAR VENDEDOR\n 5. SAIR\n   Insira uma opção: "))
    while True:
        if (opcao == 0):
            opcao = int(input("\n MENU - GERENTE \n 1. ESTOQUE \n 2. VER VENDEDORES DO SETOR\n 3. RELATORIO MENSAL\n 4. ADICIONAR VENDEDOR\n 5. SAIR\n   Insira uma opção: "))
            continue
            
        elif (opcao == 1):
            estoqueop = 0
            estoqueop = int(input("\n ESTOQUE \n 1. VER ITENS\n 2. ADICIONAR ITEM\n 3. Voltar \n  >"))
            if estoqueop == 1:
                infos = ver_est_itens()
                for item in infos:
                    print(item[:-1])
                alt = input("Deseja alterar um item?(s/n)\n >")
                if alt == "s" or alt == "S":
                    iid = int(input("\n Item ID: "))
                    coluna = input("\n Qual atributo(s)?: ")
                    valores = input("\n Qual(is) valor(es)?: ")
                    alterar_item(coluna, valores, iid)
                input("Digite qualquer coisa para voltar.\n >")

            elif estoqueop == 2:
                print("\n ADICIONAR ITEM\n")
                #INSERT INTO item (item_id, item_preco, lugar_fabricacao, categoria, cor) VALUES(0, 0, '', '', '');
                iid = int(input("\n Item ID: "))
                ipreco = float(input("\n PREÇO: "))
                lugar = input("\n Lugar de fabricação: ")
                categoria = input("\n Categoria: ")
                cor = input("\n Cor: ")
                VALUES = [iid, ipreco, lugar, categoria, cor]
                inserir_item(VALUES)

            elif estoqueop == 3:
                opcao = 0
                continue

        elif (opcao == 2): # 3. VENDEDORES DO SETOR
            vendedor_gerente(id_func)

        elif (opcao == 3): # Relatório Mensal
            mes = input("\nDigite o número do mês que você quer ver o histórico (1 a 12)\n >>> ")
            while int(mes) > 12 and int(mes) < 1:
                print("\n ---- MÊS INVÁLIDO ----")
                mes = input("\nDigite o número do mês que você quer ver o histórico (1 a 12)\n >>> ")
            relatorio_mensal('mes')
            pass

        elif (opcao == 4):
            all_func_id = lista_id_funcionarios()
            while True:
                new_vendedor_id=random.randrange(1, 10000)
                if new_vendedor_id not in all_func_id:
                    break
            add_vendedor_supervisao(id_func, new_vendedor_id)

        elif (opcao == 5):
            print("\n Bom trabalho. Até amanhã. \n")
            break
            
        elif (opcao < 0) or (opcao > 5):
            print("\nEssa opcao não existe, selecione outra\n")
            continue
        opcao = 0
#INTERFACE VENDEDOR --------------------------------------
if LOG == 2:
    opcao = int(input("\n MENU - VENDEDOR \n 1. VER PEDIDOS PARA EFETIVAR\n 2. VER ITENS COM BAIXO ESTOQUE \n 3. VER VENDAS EFETIVADAS\n 4. SAIR\n   Insira uma opção: ")) # Ver pedidos que efetivou
    while True:
        if (opcao == 0):
            opcao = int(input("\n MENU - VENDEDOR \n 1. EFETIVAR COMPRA\n 2. VER ITENS COM BAIXO ESTOQUE \n 3. VER VENDAS EFETIVADAS\n 4. SAIR\n  Insira uma opção: "))
            continue
        elif (opcao == 1):
            pedidoslista = listar_pedidos()
            if listar_pedidos() != -1: # Se não existe algum item para efetivar:
                try:
                    cod_pedido = int(input("\nDigite o codigo do pedido que você quer efetivar\n ---> "))
                except ValueError:
                    print("\n Código Digitado Inválido")
                    break
                if cod_pedido in pedidoslista: # checar se realmente está nos pedidos em andamento
                    alterar_status_pedido(cod_pedido, id_func) # ir na tabela de pedido, carrinho(vai esvaziar se efetivar, e ver qtd de item específico), estoque(-qtd), item(consultar), vendedor(add pedido a ele)
                    print('\nStatus Alterado com Sucesso!!')
                else:
                    print("\nID não encontrado!")
            else:
                print("\n Não existe item para efetivar \n")
        elif (opcao == 2):
                exibir_estoquebaixo()

                input("Digite qualquer coisa para voltar.\n >")

        elif (opcao == 3):
                dados = input("\n digite seu ")
                listar_pedido_vendedor(id_func)
                input("Digite qualquer coisa para voltar.\n >")

        elif (opcao == 4):
            print("\n Bom trabalho. Até amanhã. \n")
            break
        opcao = 0

exit

