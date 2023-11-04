#from bdinit import create_table, inserir_cliente, alterar_cliente, pesquisar_nome, remover_cliente, listar_todos, exibir_um, conexao, login_cliente login_funcionario
from bdinit import *
create_table()

print("\n BOAS VINDAS A LOJA DE ROUPAS")

#opcao = int(input("\n Menu:\n 1. Cadastro Cliente\n 2. Login Cliente \n 3. Ver Itens da Loja \n 4. Login Funcionário \n 5. Sair\n  Insira uma opção: "))
# Login Funcionario sem cadastro pois a loja vai começar com pelo menos um gerente, e ele que vai cadastrando os funcionarios
LOG = 0
ID = ""
tipo = 0

cliente = ["ID: ", "Username: ", "Senha: ", "Nome: ", "Email: ", "CPF: ", "Torcedor do Flamengo: ", "Fã de One Piece: ", "De Souza: "]
endereco = ["Cidade: ", "Estado: ", "Rua: ", "Numero: ", "CEP: "]

def nome(lista):
  item_nome = input("\nDigite o nome: ").lower()
  return [dado for dado in lista if item_nome in dado[0].lower()]

def categoria(lista):
    item_categoria = input("\nDigite a categoria: ").lower()
    return [dado for dado in lista if item_categoria in dado[1].lower()]
        
def cor(lista):
    item_cor = input("\nDigite a cor desejada: ").lower()
    return [dado for dado in lista if item_cor in dado[2].lower()]
        
def faixa_preco(lista, x, y):
    while True:
        item_faixa_preco = input("\nDigite a faixa de preço(ex.: 1, 10): ").replace(" ", "")
        parts = item_faixa_preco.split(',')
        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            print("A string de entrada deve ter dois números separados por vírgula.")
            continue
        x, y = map(int, parts)
        if x >= y:
            print("O primeiro número deve ser menor que o segundo.")
            continue
        return x, y
        return [dado for dado in lista if x <= dado[3] <= y]
        
def local_fabricacao(lista):
    item_local_fabricacao = input("\nDigite o local de fabricação: ").lower()
    return [dado for dado in lista if item_local_fabricacao in dado[4].lower()]

#INTERFACE USUARIOS
opcao = int(input("\n 1.LOGIN\n 2.CADASTRO\n 3.VER ITENS\n 4.FECHAR \n Insira uma opção:\n  > "))
while opcao != 4 and tipo != 4:
    if opcao == 0:
        opcao = int(input("\n      MENU \n 1.LOGIN\n 2.CADASTRO\n 3.VER ITENS\n 4.FECHAR \n Insira uma opção:\n  > "))
    if (opcao == 1):
        # LOGINS SEPARADOS EM CLIENTE E FUNCIONARIOS
        tipo = int(input("\n LOGIN: \n 1. Login como cliente\n 2. Login como funcionario \n 3. Voltar \n 4. Sair\n > "))

        if tipo == 1:
            #CLIENTE
            print("\n LOGIN \n")
            user = input("   Insira o usuario do cliente: ")
            senha = input("   Insira a senha do cliente: ")
            info_cliente = login_cliente(user, senha)
            if info_cliente != False:
                print("\n Login Feito com sucesso! \n")
                ID = ID_cliente(user)
                LOG = 1
                # agora está logado -> pode fazer pedidos
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
                if check_info('cod_func', id_func, 'cod_func', 'gerente') != False:
                    LOG = 3
                    interface_gerente(id_func)
                else:
                    interface_vendedor(id_func)
            else:
                print("\n Informações incorretas \n")
        
        elif tipo == 3:
            opcao = 0

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
        
        
        filtrar_item = input("Deseja filtrar os itens disponíveis? (S/N) > ")
        if filtrar_item.upper() == 'S':
            escolha_filtro = int(input("\n 1.NOME\n 2.CATEGORIA\n 3.COR\n 4.FAIXA DE PREÇO\n 5.LOCAL DE FABRICAÇÃO\n Escolha um filtro:\n > "))
            lista = listar_item()
            resultados = []
    
            if escolha_filtro == 1:
                resultados = nome(lista)
            elif escolha_filtro == 2:
                resultados = categoria(lista)
            elif escolha_filtro == 3:
                resultados = cor(lista)
            elif escolha_filtro == 4:
                resultados = faixa_preco(lista, x, y)
            elif escolha_filtro == 5:
                resultados = local_fabricacao(lista)
            
            else:
                print("Essa opção não existe, selecione outra.\n")
                opcao = int(input(" > "))
    
            if resultados:
                for resultado in resultados:
                    print(resultado)
            else:
                print("\nNão temos esse item no estoque.")
                
        else:
            input("Digite qualquer coisa para prosseguir.\n >")
            opcao = 0
            continue

        cont = 0
        print("\nITENS NO CATÁLOGO\n")
        lista = listar_item()
        
        for item in lista:
            cont += 1
            print(cont,". ",item)
    
    elif (opcao == 4):
        print("\n Volte Sempre !\n\n")
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
                ck = input("Você ainda não adicionou endereço de entrega. Deseja adicionar?\n >")
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
            # Se sobrar tempo: criar uma função p o cliente pesquisar por cor/categoria
            lista = listar_item()
            while True:
                for item in lista:
                    print(item)
                try:
                    add_aocarrinho = int(input("\n Digite o ID(INTEIRO) do item que deseja adicionar ao carrinho: \n -----> "))
                except ValueError:
                    print("\n -----------ERRO: NÃO FOI DIGITADO UM NÚMERO INTEIRO----------\n ")
                is_item = check_info('item_id', add_aocarrinho, 'item_id', item)
                if is_item != False:
                    inserir_item_carrinho(ID, is_item)
                else:
                    print("Item ID inválido")
                print(" -------- CARRINHO DE COMPRAS ------------")
                listar_carrinho(ID)
                ask = input("\nDigite se você deseja continuar (s/n):\n ----> ")
                while ask != 's' and ask != 'n':
                    ask = input("\nDigite se você deseja continuar (s/n):\n ----> ")
                if ask == 'n':
                    break
            continue
            
        elif (opcao == 3):
            print("\n HISTORICO DE PEDIDOS: \n")
            
            
            continue
        
        elif (opcao == 4):
            interface_carrinho(ID)

            continue

        elif (opcao == 5):
            print("\nObrigada por usar nosso sistema. Volte sempre!\n")
            break
            
        elif (opcao < 0) or (opcao > 5):
            print("\nEssa opcao não existe, selecione outra\n")
            continue

        opcao = 0
exit

#INTERFACE GERENTE
if LOG == 3:
    opcao = int(input("\n MENU - GERENTE \n 1. SETOR\n 2. ESTOQUE \n 3. VENDEDORES DO SETOR\n 4. RELATORIO MENSAL\n 5. SAIR\n   Insira uma opção: "))
    while True:
        if (opcao == 0):
            opcao = int(input("\n MENU - GERENTE \n 1. SETOR\n 2. ESTOQUE \n 3. VENDEDORES DO SETOR\n 4. RELATORIO MENSAL\n 5. SAIR\n   Insira uma opção: "))
            continue
        elif (opcao == 1):
            print("\n SETOR\n")
            
        elif (opcao == 2):
            print("\n ESTOQUE\n")
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

        #elif (opcao == 3):

        #elif (opcao == 4):

        elif (opcao == 5):
            print("\n Bom trabalho. Até amanhã. \n")
            break
            
        elif (opcao < 0) or (opcao > 5):
            print("\nEssa opcao não existe, selecione outra\n")
            continue




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