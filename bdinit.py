import random
import sqlite3
from datetime import datetime
from func_filters import nome, categoria, cor, faixa_preco, local_fabricacao, obter_faixa_preco

conexao = sqlite3.connect("clientes.db")
ponte = conexao.cursor()

def create_table():
    create = """CREATE TABLE IF NOT EXISTS cliente(
cliente_id integer PRIMARY KEY AUTOINCREMENT, 
username VarChar(25) NOT NULL,
senha VarChar(15) NOT NULL,
nome VarChar(50) NOT NULL,
email VarChar(50) NOT NULL,
cpf VarChar(20) NOT NULL,
is_flamengo BOOL NOT NULL DEFAULT FALSE,
is_op BOOL NOT NULL DEFAULT FALSE,
is_souza BOOL NOT NULL DEFAULT FALSE,
UNIQUE (cpf),
UNIQUE (username),
CONSTRAINT ck_nome CHECK (length(nome) < 50 and length(nome) >= 3 )
CONSTRAINT ck_username CHECK (length(username)< 15 and length(username) >= 3)
CONSTRAINT ck_senha CHECK (length(senha)>4 and length(senha)<15),
CONSTRAINT ck_cpf CHECK (length(cpf)== 11)
CONSTRAINT ck_email CHECK (Email LIKE '%_@_%._%')
);

CREATE TABLE IF NOT EXISTS endereco(
cidade VarChar(50) NOT NULL,
estado VarChar(50) NOT NULL,
rua VarChar(50) NOT NULL,
numero integer NOT NULL,
CEP integer NOT NULL,
clienteFK integer NOT NULL,
FOREIGN KEY(clienteFK) REFERENCES cliente(cliente_id)
ON DELETE SET NULL
ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS item(
item_id integer PRIMARY KEY NOT NULL,
item_nome VarChar(50) NOT NULL,
preco float NOT NULL,
lugar_fabricacao VarChar(50) NOT NULL,
categoria VarChar(50) NOT NULL,
cor VarChar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS pedido(
pedido_id integer PRIMARY KEY NOT NULL,
qtd_itens integer NOT NULL,
valor_total float NOT NULL,
pagamento VarChar(50) NOT NULL,
status_pagamento VarChar(50) NOT NULL,
status VarChar(50) NOT NULL,
mes VarChar(3) NOT NULL,
clienteFK integer NOT NULL,
FOREIGN KEY(clienteFK) REFERENCES cliente(cliente_id)
ON DELETE SET NULL
ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS carrinho(
qtd_item integer NOT NULL,
item_idFK integer NOT NULL,
pedidoFK integer NOT NULL DEFAULT "Pedido não feito",
clienteFK integer NOT NULL,
FOREIGN KEY(pedidoFK) REFERENCES pedido(pedido_id)
ON DELETE SET NULL
ON UPDATE CASCADE,
FOREIGN KEY(item_idFK) REFERENCES item(item_id)
ON DELETE SET NULL
ON UPDATE CASCADE,
FOREIGN KEY(clienteFK) REFERENCES cliente(cliente_id)
ON DELETE SET NULL
ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS estoque(
qtd_estoque integer NOT NULL DEFAULT 0,
item_idFK integer NOT NULL,
FOREIGN KEY(item_idFK) REFERENCES item(item_id)
ON DELETE SET NULL
ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS funcionario(
cod_func integer PRIMARY KEY NOT NULL,
nome VarChar(30) NOT NULL,
senha VarChar(15) NOT NULL,
email VarChar(50) NOT NULL,
cpf VarChar(20) NOT NULL,
CONSTRAINT email CHECK (email LIKE '%_@_%._%'),
CONSTRAINT senha CHECK (length(senha) < 15 and length(senha) >= 3 )
);

CREATE TABLE IF NOT EXISTS vendedor(
conf_venda VarChar(50) NOT NULL DEFAULT '0',
funcFK integer NOT NULL,
pedido_idFK integer NOT NULL DEFAULT 0,
mes_efetivado VarChar(3) NOT NULL DEFAULT '0',
FOREIGN KEY(funcFK) REFERENCES funcionario(cod_func)
ON DELETE SET NULL
ON UPDATE CASCADE,
FOREIGN KEY(pedido_idFK) REFERENCES pedido(pedido_id)
ON DELETE SET NULL
ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS gerente(
funcFK integer NOT NULL,
vendedorFK integer NOT NULL DEFAULT 0,
FOREIGN KEY(funcFK) REFERENCES funcionario(cod_func)
ON DELETE SET NULL
ON UPDATE CASCADE,
FOREIGN KEY(vendedorFK) REFERENCES vendedor(cod_func)
ON DELETE SET NULL
ON UPDATE CASCADE
);

INSERT OR IGNORE INTO item(item_id, item_nome, preco, lugar_fabricacao, categoria, cor )
VALUES(1758, 'Camisa Twilight', '67.00', 'Mari', 'camisa', 'rosa'),
(1479, 'Camisa Sparky', '67.67', 'Lalaland', 'camisa', 'roxo'),
(1378, 'Camisa Luffy', '53.99', 'Mari', 'camisa', 'vermelho'),
(1798, 'Camisa Morgana', '67.90', 'Mari', 'camisa', 'preto'),
(1712, 'Camisa Grifinoria', '93.40', 'Hogwarts', 'camisa', 'vermelha'),
(1713, 'Camisa Lufalufa', '93.40', 'Hogwarts', 'camisa', 'amarela'),
(1714, 'Camisa Sonserina','93.40', 'Hogwarts', 'camisa', 'verde'),
(1715, 'Camisa Corvinal','93.40', 'Hogwarts', 'camisa', 'azul'),
(1211, 'Camisa Caldas','89.90', 'Caldas Novas', 'camisa', 'branco'),
(1755, 'Camisa Contra o Sol','55.90', 'Patos de Minas', 'camisa', 'preto'),
(2567, 'Calça Twilight','53.99', 'Diadema', 'calça', 'roxo'),
(2324, 'Calça Jeans','59.99', 'Mari', 'calça', 'azul'),
(2343, 'Calça Jeans','69.67', 'Mariliu', 'calça', 'azul'),
(2344, 'Calça Pateta','99.99', 'Orlando', 'calça', 'preto'),
(2712, 'Calça Mago','93.40', 'Hogwarts', 'calça', 'preto'),
(4361, 'Short jeans','50.99', 'Mari', 'short', 'azul'),
(4320, 'Short liso','49.99', 'São Paulo', 'short', 'preto'),
(4323, 'Short liso','45.89', 'São Paulo', 'short', 'branco'),
(1755, 'Short preto','44.90', 'Diadema', 'short', 'preto');

INSERT OR IGNORE INTO estoque(item_idFK, qtd_estoque)
VALUES(1758, 13),
(1479, 15),
(1378, 23),
(1798, 5),
(1712, 9),
(1713, 15),
(1714, 10),
(1715, 17),
(1211, 30),
(1755, 30),
(2567, 15),
(2324, 20),
(2343, 22),
(2344, 35),
(2712, 10),
(4361, 15),
(4320, 15),
(4323, 25),
(1755, 9);

INSERT OR IGNORE INTO cliente(username, senha, nome, email, cpf, is_flamengo, is_op, is_souza)
VALUES('flam', 'mengão', 'Gabriel Barbosa', 'gabigol@fmail.com', '01210455122', 'False', 'True', 'True' ),
('luffy', 'amoonepiece', 'sanji', 'marry@fmail.com', '33218800099', 'True', 'True', 'False'),
('torta', 'pineapple', 'Pinkie Pie', 'PINKIE@fmail.com', '01210001122', 'True', 'False', 'False'),('amanhecer', '1senha23', 'Twilight', 'ponypony@fmail.com', '01238237890', 'False', 'False', 'True'),('Equestria', '123senha', 'Equestria', '4o4@fmail.com', '01234567890', 'True', 'True', 'True'),('maça', 'abc1232', 'Apple Jack', 'macieira@pmail.com', '22344566700', 'False', 'True', 'True'),('Spark', 'milan777', 'Rarity', 'brilho@pmail.com', '11122233344', 'False', 'False', 'False'),('Angel', 'iisenha6', 'Angela', 'anf@gmail.com', '01666237890', 'False', 'False', 'False'),('Gabriel', 'senha339', 'Cabri', 'leaf@fmail.com', '01010129277', 'False', 'False', 'False'),('amigue','senha332', 'Monica', 'sansao@fmail.com', '00003333222', 'False', 'True', 'True'),('bolinha1', 'rsenha331','Cebolinha', '5sorte@fmail.com', '01672929772', 'True', 'False', 'True'),('maga', 'senha330', 'Magali', 'kkkkk@gmail.com', '11119999222', 'False', 'False', 'False'),('cascadebala4', 'senha334', 'Cascao', 'oinc@fmail.com', '01018888292', 'True', 'False', 'True'),('len', 'senha221', 'Milena', 'natureza@fmail.com', '01013333666', 'True', 'True', 'True'),('fran', 'senha888', 'Franjinha', 'ciencia@fmail.com', '33334444551', 'True', 'True', 'False'),('Tom', '123senha', 'Timothy', 'ema@fmail.com', '01010129292', 'False', 'False', 'False'),('Jerry', 'ratinho123', 'Jeremias de Souza','jerro@fmail.com', '03168442024', 'True', 'True', 'True'),('RainbowDash', 'Imnotponny2', 'Anna Luiza de Albuquerque', 'aninhaalbuq@fmail.com', '00345162366', 'False', 'False', 'False'),('Vineo', 'thisisme123', 'Angelina Jullie', 'jullita2334@fmail.com', '11546325851', 'False', 'False', 'False');

INSERT OR IGNORE INTO funcionario(cod_func, nome, senha, email, cpf)
VALUES(1, 'First', '123', 'super_gerente@hotmail.com', '00000000001'),
(2, 'Second', 123, 'second@hotmail.com', '00000000002'),
(3, 'Third', 123, 'third@hotmail.com', '00000000003'),
(4, 'Fourth', 123, 'Fourth@hotmail.com', '00000000004'),
(5, 'Fifth', 123, 'fifth@hotmail.com', '00000000005'),
(6, 'Sixth', 123, 'sixth@hotmail.com', '00000000006'),
(7, 'Seventh', 123, 'seventh@hotmail.com', '00000000007'),
(8, 'Eighth', 123, 'eighth@hotmail.com', '00000000008');
INSERT OR IGNORE INTO gerente(funcFK)
VALUES(1),
(2);
INSERT OR IGNORE INTO vendedor(funcFK)
VALUES(3),(4),(5),(6),(7),(8);
INSERT OR IGNORE INTO gerente(funcFK, vendedorFK)
VALUES(1, 3),
(1, 4),
(1, 5);
"""
# Falta criar os itens
    #ponte.execute(create)
    ponte.executescript(create)
    conexao.commit()
    inserir_item_carrinho(1, 1479, 1)
    inserir_item_carrinho(1, 1378, 1)
    inserir_item_carrinho(2, 2344, 4)
    inserir_item_carrinho(3, 1755, 2)
    inserir_item_carrinho(4, 1798, 3)
    inserir_item_carrinho(4, 1378, 1)
    inserir_item_carrinho(4, 1755, 1)
    inserir_item_carrinho(5, 4320, 2)
    inserir_item_carrinho(5, 1211, 1)
    add_pedido(1, 'Cartão', 42)
    add_pedido(2, 'Cartão', 53)
    alterar_status_pedido(42, 3)
    

#LOGINS ----------------------------------------
def login_funcionario(email, senha):
    if check_info('email', email, 'cod_func', 'funcionario') != False and check_info('senha', senha, 'cod_func', 'funcionario') != False:
        return check_info('email', email,'cod_func', 'funcionario')
    return False

def login_cliente(user, senha):
    if check_info('username', user, 'cliente_id','cliente') != False and check_info('senha', senha, 'cliente_id', 'cliente') != False:
        return check_info('username', user, 'cliente_id','cliente')
    return False

def check_info(col, info, col_return, table):
    if type(info) == int:
        checar = f"SELECT {col_return} FROM {table} WHERE ({col} = {info});"
    else:
        checar = f"SELECT {col_return} FROM {table} WHERE ({col} = '{info}');"
    ponte.execute(checar)
    checar = ponte.fetchall()
    if len(checar) != 0:
        return checar[0][0]
    return False

#INTERFACE ----------------------------------------
def interface_gerente(info):
    pass
    # Supervisiona Vendedores e Abastece estoque
    # Terá lista de vendedores(que ele supervisiona) em que ele pode acessar as vendas de cada um

def interface_vendedor(info):
    pass
    # Vendas para efetivar
    # pode acessar suas prórias vendas (pedidos que efetivou)

def interface_carrinho(ID):
    print("\n\n---------------------- CARRINHO ----------------------\n")
    carrinho_escolha = int(input("\n 1. Remover Item\n 2. Fechar Pedido\n 3. Ver Carrinho \n 4. Sair do Carrinho \n ---> Insira uma opção: "))
    while carrinho_escolha != 4:
        if carrinho_escolha == 1:
            # LISTAR CARRINHO
            listar_carrinho(ID)
            # REMOVER ITEM
            remover_item = int(input("Digite o ID do item que você quer remover\n ----> "))
            remover_item_carrinho(ID, remover_item)
        elif carrinho_escolha == 2:
            
            all_pedido_id = lista_pedidos()
            while True:
                new_pedido_id=random.randrange(1, 10000)
                if new_pedido_id not in all_pedido_id:
                    break
            
            tipopagamento = int(input("\n Boa escolha! Como será o pagamento? 1. Cartão\n 2. Boleto\n 3. Pix \n 4. Berries \n ---> Insira uma opção: "))
            while tipopagamento != 1 and tipopagamento != 2 and tipopagamento != 3 and tipopagamento != 4:
                tipopagamento = int(input("\n Como será o pagamento? 1. Cartão\n 2. Boleto\n 3. Pix \n 4. Berries \n ---> Insira uma opção: "))
                if tipopagamento == 1:
                    pagamento = "Cartão"
                elif tipopagamento == 2:
                    pagamento = "Boleto"
                elif tipopagamento == 3:
                    pagamento = "Pix"  
                elif tipopagamento == 4:
                    pagamento = "Berries"      
                else:
                    print("\nInput Inválido, Tente Novamente...\n")

            add_pedido(ID, pagamento, new_pedido_id)
            
        elif carrinho_escolha == 3:
            listar_carrinho(ID)
        elif carrinho_escolha != 4:
            print("\n ----- OPÇÃO INVÁLIDA, TENTE NOVAMENTE ------- \n")
        carrinho_escolha = int(input("\n 1. Remover Item\n 2. Fechar Pedido\n 3. Ver Carrinho \n 4. Sair do Carrinho"))
    print("\n --------- Saindo do Carrinho... ---------\n")

#ITENS ----------------------------------------
def listar_item():
    pesquisar = f"SELECT item_nome, categoria, cor, preco FROM item;"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    return(pesquisa)

def inserir_item(info,einfo):
    inseriri = "INSERT INTO item (item_id, item_nome, preco, lugar_fabricacao, categoria, cor) VALUES(?,?,?,?,?,?)"
    ponte.execute(inseriri, info)
    inserire = f"INSERT INTO estoque(item_idFK, qtd_estoque) VALUES(?,?)"
    ponte.execute(inserire, einfo)
    conexao.commit()

def alterar_item(coluna, novo, chave):
    alterar = f"UPDATE item SET {coluna} = {novo} WHERE (item_id == '{chave}');"
    ponte.execute(alterar)
    conexao.commit()

def ver_est_itens():
    pesquisar = f"SELECT item.*,estoque.* FROM item FULL OUTER JOIN estoque ON item_id = item_idFK;"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    return(pesquisa)

def estoque_item_especifico(item_id):
    pesquisar = f"SELECT E.qtd_estoque FROM item I INNER JOIN estoque E ON item_id = item_idFK WHERE item_idFK = {item_id};"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    return(pesquisa[0][0])
    
#CLIENTES/PEDIDOS ----------------------------------------

def inserir_cliente(info):
    inserir = "INSERT INTO cliente(nome, username, senha, email, cpf, is_flamengo, is_op, is_souza) VALUES(?,?,?,?,?,?,?,?)"
    ponte.execute(inserir, info)
    conexao.commit()

def alterar_cliente(coluna, novo, chave):
    alterar = f"UPDATE cliente SET {coluna} = '{novo}' WHERE (username == '{chave}');"
    ponte.execute(alterar)
    conexao.commit()

def pesquisar_nome(chave):
    pesquisar = f"SELECT * FROM cliente WHERE (nome LIKE '{chave}');"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    print(pesquisa)
    return(pesquisa)

def lista_pedidos():
    pesquisar = f"SELECT pedido_id FROM pedido;"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    lista = []
    for valor in pesquisa:
        lista.append(valor[0])
    return(lista)

def lista_id_funcionarios():
    pesquisar = f"SELECT cod_func FROM funcionario;"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    lista = []
    for valor in pesquisa:
        lista.append(valor[0])
    return(lista)

def remover_cliente(info):
    deletar = f"DELETE FROM cliente WHERE (username = '{info}');"
    ponte.execute(deletar)
    conexao.commit()

def listar_todos():
    pesquisar = f"SELECT * FROM cliente;"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    return(pesquisa)

def ID_cliente(chave):
    pesquisar = f"SELECT cliente_id FROM cliente WHERE (username == '{chave}');"
    ponte.execute(pesquisar)
    id_l = ponte.fetchone()
    print(id_l[0])
    return(id_l[0])

def exibir_um(chave):
    pesquisar = f"SELECT * FROM cliente WHERE (username == '{chave}');"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    print(pesquisa)
    return(pesquisa)

def desconto():
    descontar = "SELECT pedido.valor_total FROM pedido WHERE EXISTS ( SELECT is_flamengo, is_op, is_souza FROM cliente WHERE cliente.cliente_id == pedido.clienteFK AND is_flamengo == True OR is_op == True OR is_souza == True)"
    ponte.execute(descontar)
    print("Desconto")
    descontostotais = ponte.fetchall()
    print(descontostotais)
    conexao.commit()

def add_pedido(cliente_id, pagamento, pedido_id):
    mes_atual = datetime.today().month
    qtd_itens_total = f"SELECT SUM(qtd_item) FROM carrinho WHERE clienteFK = {cliente_id}"
    ponte.execute(qtd_itens_total)
    qtd_itens_total = ponte.fetchall()
    qtd_itens_total = qtd_itens_total[0][0]
    v_total = f"""SELECT SUM(I.preco * C.qtd_item)
        FROM item I INNER JOIN carrinho C
        ON I.item_id = C.item_idFK WHERE C.clienteFK = {cliente_id};"""
    ponte.execute(v_total)
    v_total = ponte.fetchall()
    v_total = v_total[0][0]
    new_pedido = f"INSERT INTO pedido(pedido_id, qtd_itens, valor_total, pagamento, status_pagamento, status, mes, clienteFK) VALUES({pedido_id},{qtd_itens_total},{v_total},'{pagamento}','Em andamento','Não Confirmado',{mes_atual}, {cliente_id});"
    ponte.execute(new_pedido)
    conexao.commit()
    pesquisar = f"SELECT * FROM pedido WHERE clienteFK = {cliente_id};"
    ponte.execute(pesquisar)
    pesquisar = ponte.fetchall()
    # add pedido no carrinho
    pedido_carrinho = f"UPDATE carrinho SET pedidoFK = {pedido_id} WHERE clienteFK = {cliente_id}"
    ponte.execute(pedido_carrinho)
    conexao.commit()

def listar_pedido_cliente(cliente_id):
    pesquisar = f"SELECT * FROM pedido WHERE clienteFK = {cliente_id};"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    count = 0
    for i in pesquisa:
        print("\n------------------------------ PEDIDO --------------------------------\n")
        print(f"|| Código do Pedido: {pesquisa[count][0]} || Quantidade de Itens: {pesquisa[count][1]} || Valor Pagamento: {pesquisa[count][2]} || Status Pagamento: {pesquisa[count][4]} || Efetivado Pelo Vendedor: {pesquisa[count][5]} || Mês do Pedido:: {pesquisa[count][6]}")
        count += 1
        item = f"""SELECT I.item_id, I.item_nome, C.qtd_item, I.preco * C.qtd_item, I.categoria, I.cor
                        FROM item I INNER JOIN carrinho C
                        ON I.item_id = C.item_idFK WHERE C.clienteFK = {cliente_id};"""
        ponte.execute(item)
        item = ponte.fetchall()
        print("\n-------------------------ITENS DO PEDIDO---------------------\n")
        count2 = 0
        for i in item:
                print(f"||Código do Item: {item[count2][0]}|| Nome: {item[count2][1]}|| Quantidade: {item[count2][2]} || Preço: {item[count2][3]} || Categoria: {item[count2][4]} || Cor:  {item[count2][5]}")
                count2 += 1

# PERFIL ----------------------------------------------------------
def ver_perfil(ID):
    ver = f"SELECT * FROM cliente WHERE (cliente_id == '{ID}');"
    ponte.execute(ver)
    perfil = ponte.fetchall()
    perfil = list(perfil[0])
    return (perfil)

def edit_perfil(ID):
    editar = f"SELECT * FROM cliente WHERE (cliente_id == '{ID}');"
    ponte.execute(editar)
    perfil = ponte.fetchall()
    return (perfil)

# ENDERECO --------------------------------------------------------

def checar_endereco(ID):
    chEnd = f"SELECT cliente_id FROM cliente WHERE EXISTS (SELECT * FROM endereco WHERE cliente_id == clienteFK AND clienteFK == '{ID}');"
    ponte.execute(chEnd)
    checou = ponte.fetchall()
    return bool(checou)

def ver_end(ID):
    ver = f"SELECT cidade, estado, rua, numero, CEP, clienteFK FROM endereco WHERE clienteFK == '{ID}';"
    ponte.execute(ver)
    end = ponte.fetchall()
    end = list(end[0])
    return (end)

def adicionar_endereco(ID):
    cidade = input("Insira sua cidade:\n >")
    estado = input("Insira seu estado:\n >")
    rua = input("Insira sua rua(Sem número):\n >")
    numero = int(input("Insira o número da rua:\n >"))
    CEP = int(input("Insira seu CEP:\n >"))
    adEnd = f"INSERT INTO endereco(cidade, estado, rua, numero, CEP, clienteFK) VALUES('{cidade}', '{estado}', '{rua}', {numero}, {CEP}, '{ID}');"
    ponte.execute(adEnd)
    print("\n ENDEREÇO ADICIONADO ! \n")
    conexao.commit()


# CARRINHO -------------
def inserir_item_carrinho(cliente_id, item_id, qtd_item):
    adIt_in_car = f"INSERT INTO carrinho(qtd_item, item_idFK, clienteFK) VALUES({qtd_item}, '{item_id}', '{cliente_id}');"
    ponte.execute(adIt_in_car)
    print("\n ITEM ADICIONADO AO CARRINHO COM SUCESSO ! \n")
    conexao.commit()

def remover_item_carrinho(cliente_id, item_id):
    qtd_item = 0
    # Qual a quantidade maxima que pode retirar do carrinho
    qtd_maxima = f"SELECT qtd_item FROM carrinho WHERE clienteFK = {cliente_id} and item_idFK = {item_id};"""
    ponte.execute(qtd_maxima)
    qtd_maxima = ponte.fetchall()
    qtd_maxima = qtd_maxima[0][0]
    while qtd_item <= 0 and qtd_item > qtd_maxima:
        qtd_item = int(input("\nDigite a quantidade do item que deseja remover do carrinho\n-------> "))
    if ((qtd_item - qtd_maxima) == 0): # remover o item completamente
        remov_it = f"DELETE FROM CARRINHO WHERE clienteFK = {cliente_id} and item_idFK = {item_id};"
    else:
        remov_it = f"UPDATE carrinho SET qtd_item = qtd_item - {qtd_item} WHERE clienteFK = {cliente_id} and item_idFK = {item_id};"
    ponte.execute(remov_it)
    print(f"\n {qtd_item} de ITEM REMOVIDO DO CARRINHO COM SUCESSO ! \n")
    conexao.commit()

def listar_carrinho(cliente_id):
    carrinho = f"""SELECT I.item_id, I.item_nome, C.qtd_item, I.preco * C.qtd_item, I.categoria, I.cor
    FROM item I INNER JOIN carrinho C
    ON I.item_id = C.item_idFK WHERE C.clienteFK = {cliente_id};"""
    ponte.execute(carrinho)
    carrinho = ponte.fetchall()
    preco_total = 0
    for i in range(len(carrinho)):
        print(f"\nCódigo: {carrinho[i][0]} || Nome: {carrinho[i][1]} || Quantidade: {carrinho[i][2]} || Preço: R${carrinho[i][3]} || Categoria: {carrinho[i][4]} || Cor: {carrinho[i][5]}")
        preco_total += carrinho[i][3]
    print(f"|| Preço Total no carrinho: R${preco_total}||")


#FILTRO ----------------------------
def filtrar_itens():
    while True:
        lista = listar_item()
        resultados =[]
    
        escolha_filtro = int(input("\n 1.NOME\n 2.CATEGORIA\n 3.COR\n 4.FAIXA DE PREÇO\n 5.LOCAL DE FABRICAÇÃO\n 6. SAIR DOS FILTROS\n Escolha um filtro:\n > "))

        if (escolha_filtro == 1):
            resultados = nome(lista)
        elif (escolha_filtro == 2):
            resultados = categoria(lista)
        elif (escolha_filtro == 3):
            resultados = cor(lista)
        elif (escolha_filtro == 4):
            x, y = obter_faixa_preco()
            resultados = faixa_preco(lista, x, y)
        elif (escolha_filtro == 5):
            resultados = local_fabricacao(lista)
        elif (escolha_filtro == 6):
            break
        elif (escolha_filtro < 1) or (escolha_filtro > 6):
            print("\nEssa opcao não existe, selecione outra.\n")
            continue 
        
        if resultados:
            for resultado in resultados:
                print(resultado)
        else:
            print("\nNão temos esse item no estoque.")

#da interface vendedor--------------------

def exibir_estoquebaixo():
    pesquisar = f"SELECT item_idFK FROM estoque WHERE (qtd_estoque < 5);"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    print(pesquisa)
    return(pesquisa)

def listar_pedidos():
    pesquisar = f"SELECT * FROM pedido WHERE status != 'Concluído';"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    if len(pesquisa) == 0:
        return -1
    count = 0
    lista_pedidos = []
    for i in pesquisa:
        lista_pedidos.append(pesquisa[count][0])
        print("\n------------------------------ PEDIDO --------------------------------\n")
        print(f"|| Código do Pedido: {pesquisa[count][0]} || Quantidade de Itens: {pesquisa[count][1]} || Valor Pagamento: {pesquisa[count][2]} || Status Pagamento: {pesquisa[count][4]} || Efetivado Pelo Vendedor: {pesquisa[count][5]} || Mês do Pedido: {pesquisa[count][6]}")
        count += 1
        item = f"""SELECT I.item_id, I.item_nome, C.qtd_item, I.preco * C.qtd_item, I.categoria, I.cor
                        FROM item I INNER JOIN carrinho C
                        ON I.item_id = C.item_idFK;"""
        ponte.execute(item)
        item = ponte.fetchall()
        print("\n-------------------------ITENS DO PEDIDO---------------------\n")
        count2 = 0
        for i in item:
                print(f"||Código do Item: {item[count2][0]}|| Nome: {item[count2][1]}|| Quantidade: {item[count2][2]} || Preço: {item[count2][3]} || Categoria: {item[count2][4]} || Cor:  {item[count2][5]}")
                count2 += 1

    return lista_pedidos

def alterar_status_pedido(cod_pedido, id_vendedor):
    mes_atual = datetime.today().month

    item = f"""SELECT   I.item_id, C.qtd_item 
                        FROM item I INNER JOIN carrinho C
                        ON (I.item_id = C.item_idFK) WHERE C.pedidoFK = {cod_pedido};"""
    ponte.execute(item)
    item = ponte.fetchall()
     
    count = 0
    for i in item:
        subtrair = f"UPDATE estoque SET qtd_estoque = qtd_estoque - {item[count][1]} WHERE(item_idFK = {item[count][0]});"
        ponte.execute(subtrair)
        conexao.commit()
        count+=1

    update_status = f"UPDATE pedido SET status = 'Concluído', status_pagamento = 'Concluído', mes = {str(mes_atual)} WHERE(pedido_id = {cod_pedido});"
    ponte.execute(update_status)
    conexao.commit()

    # Esvaziar carrinho ja que a compra foi efetivada
    select_cliente = f"SELECT P.clienteFK FROM pedido P WHERE pedido_id = {cod_pedido}"
    ponte.execute(select_cliente)
    select_cliente = ponte.fetchall()
    cliente_id = select_cliente[0][0]
    update_carrinho = f"DELETE FROM carrinho WHERE clienteFK = {cliente_id}"

    # Colocar pedido no vendedor
    inserir = f"INSERT INTO vendedor(funcFK, pedido_idFK, mes_efetivado) VALUES({id_vendedor},{cod_pedido},{mes_atual})"
    ponte.execute(inserir)
    conexao.commit()


def listar_pedido_vendedor(vendedor_id):
    pesquisar = f"SELECT pedido_idFK FROM vendedor WHERE cod_func = {vendedor_id};"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()


    """
    update_mes = f"UPDATE pedido SET mes = {mes} WHERE(pedido_id = {cod_pedido});"
    ponte.execute(subtrair)
    conexao.commit()

    
    for i in pesquisar:
        subtrair = f"UPDATE estoque SET qtd_estoque = qtd_estoque - '{item}' WHERE((item_idFK == '{cod_pedido}');"
        ponte.execute(subtrair)
        conexao.commit()
    """
        

# Gerente
def vendedor_gerente(gerente_id):
    vendedores = f"SELECT vendedorFK FROM gerente WHERE funcFK = {gerente_id}"
    ponte.execute(vendedores)
    vendedores = ponte.fetchall()
    if len(vendedores) <= 1: # pois terá só o id 0, mas o id 0 significa que não tem nenhum vendedor associado ao gerente
        print("\n Não há vendores sob sua supervisão \n")
        return -1
    
    print("-------- Vendedores ----------")
    linha = 0
    for i in vendedores:
        vendedores_info = f"""SELECT F.cod_func, F.nome, F.cpf FROM funcionario F, vendedor V 
                            ON F.cod_func = V.funcFK WHERE (V.funcFK = {vendedores[linha][0]})"""
        ponte.execute(vendedores_info)
        vendedores_info = ponte.fetchall()
        if linha != 0:
            print(vendedores_info)
        linha+=1
    return 0

def add_vendedor_supervisao(id_gerente, new_vendedor_id):
    nome = input("  Insira o nome do cliente: ")
    email = input("  Insira o email do cliente: ")
    senha = input("  Insira a senha do cliente: ")
    cpf = input("  Insira o cpf do cliente: ")
    dados = [new_vendedor_id, nome, email, senha, cpf]
    inserir_func = "INSERT INTO funcionario (cod_func, nome, email, senha, cpf) VALUES(?,?,?,?,?)"
    ponte.execute(inserir_func, dados)
    inserir_vend = "INSERT INTO vendedor (funcFK) VALUES(?)"
    ponte.execute(inserir_vend, new_vendedor_id)
    inserir_in_gerente = "INSERT INTO gerente (funcFK, vendedorFK) VALUES(?,?)"
    ponte.execute(inserir_in_gerente, [id_gerente, new_vendedor_id])
    conexao.commit()