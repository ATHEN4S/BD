import random
import sqlite3

conexao = sqlite3.connect('clientes.db')

ponte = conexao.cursor()

def create_table():
    with conexao:
        create = """CREATE TABLE cliente(
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

CREATE TABLE endereco(
endereco_id integer PRIMARY KEY,
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

CREATE TABLE item(
item_id integer PRIMARY KEY NOT NULL,
item_preco float NOT NULL,
lugar_fabricacao VarChar(50) NOT NULL,
categoria VarChar(50) NOT NULL,
cor VarChar(50) NOT NULL
);

CREATE TABLE pedido(
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

CREATE TABLE carrinho(
qtd_item integer NOT NULL,
item_idFK integer NOT NULL,
pedidoFK integer NOT NULL,
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

CREATE TABLE estoque(
qtd_estoque integer NOT NULL DEFAULT 0,

item_idFK integer NOT NULL,
FOREIGN KEY(item_idFK) REFERENCES item(item_id)
);

CREATE TABLE funcionario(
cod_func integer PRIMARY KEY NOT NULL,
nome VarChar(30) NOT NULL,
senha VarChar(15) NOT NULL,
email VarChar(50) NOT NULL,
cpf VarChar(20) NOT NULL,
CONSTRAINT email CHECK (email LIKE '%_@_%._%'),
CONSTRAINT senha CHECK (length(senha) < 15 and length(senha) >= 3 )
);

CREATE TABLE vendedor(
conf_venda VarChar(50) NOT NULL DEFAULT 0,
funcFK integer NOT NULL,
pedido_idFK integer NOT NULL,

FOREIGN KEY(funcFK) REFERENCES funcionario(cod_func)
ON DELETE SET NULL
ON UPDATE CASCADE,
FOREIGN KEY(pedido_idFK) REFERENCES pedido(pedido_id)
ON DELETE SET NULL
ON UPDATE CASCADE
);

CREATE TABLE gerente(
chave integer PRIMARY KEY NOT NULL,
funcFK integer NOT NULL,
vendedorFK integer,
FOREIGN KEY(funcFK) REFERENCES funcionario(cod_func)
ON DELETE SET NULL
ON UPDATE CASCADE,
FOREIGN KEY(vendedorFK) REFERENCES vendedor(cod_func)
ON DELETE SET NULL
ON UPDATE CASCADE
);

INSERT INTO funcionario(cod_func, nome, senha, email, cpf)
VALUES(1, 'First', '123', 'super_gerente@hotmail.com', '00000000001');
INSERT INTO gerente(chave, funcFK, vendedorFK)
VALUES(21, 1, 0);


INSERT INTO item(item_id, item_preco, lugar_fabricacao, categoria, cor )
VALUES(1758, '67.00', 'Mari', 'camisa', 'rosa'),
(1478, '67.67', 'Mariliu', 'camisa', 'roxo'),
(1798, '67.90', 'Muri', 'camisa', 'preta'),
(4567, '62.67', 'Mariliu', 'calça', 'roxo'),
(2324, '69.67', 'Mariliu', 'calça', 'preto');

INSERT INTO cliente(username, senha, nome, email, cpf, is_flamengo, is_op, is_souza)
VALUES('flam', 'mengão', 'Gabriel Barbosa', 'gabigol@fmail.com', '01210455122', 'False', 'True', 'True' ),
('luffy', 'amoonepiece', 'sanji', 'marry@fmail.com', '33218800099', 'True', 'True', 'False'),
('torta', 'pineapple', 'Pinkie Pie', 'PINKIE@fmail.com', '01210001122', 'True', 'False', 'False'),('amanhecer', '1senha23', 'Twilight', 'ponypony@fmail.com', '01238237890', 'False', 'False', 'True'),('Equestria', '123senha', 'Equestria', '4o4@fmail.com', '01234567890', 'True', 'True', 'True'),('maça', 'abc1232', 'Apple Jack', 'macieira@pmail.com', '22344566700', 'False', 'True', 'True'),('Spark', 'milan777', 'Rarity', 'brilho@pmail.com', '11122233344', 'False', 'False', 'False'),('Angel', 'iisenha6', 'Angela', 'anf@gmail.com', '01666237890', 'False', 'False', 'False'),('Gabriel', 'senha339', 'Cabri', 'leaf@fmail.com', '01010129277', 'False', 'False', 'False'),('amigue','senha332', 'Monica', 'sansao@fmail.com', '00003333222', 'False', 'True', 'True'),('bolinha1', 'rsenha331','Cebolinha', '5sorte@fmail.com', '01672929772', 'True', 'False', 'True'),('maga', 'senha330', 'Magali', 'kkkkk@gmail.com', '11119999222', 'False', 'False', 'False'),('cascadebala4', 'senha334', 'Cascao', 'oinc@fmail.com', '01018888292', 'True', 'False', 'True'),('len', 'senha221', 'Milena', 'natureza@fmail.com', '01013333666', 'True', 'True', 'True'),('fran', 'senha888', 'Franjinha', 'ciencia@fmail.com', '33334444551', 'True', 'True', 'False'),('Tom', '123senha', 'Timothy', 'ema@fmail.com', '01010129292', 'False', 'False', 'False'),('Jerry', 'ratinho123', 'Jeremias de Souza','jerro@fmail.com', '03168442024', 'True', 'True', 'True'),('RainbowDash', 'Imnotponny2', 'Anna Luiza de Albuquerque', 'aninhaalbuq@fmail.com', '00345162366', 'False', 'False', 'False'),('Vineo', 'thisisme123', 'Angelina Jullie', 'jullita2334@fmail.com', '11546325851', 'False', 'False', 'False');
"""
# Falta criar os itens
        #ponte.execute(create)
        ponte.executescript(create)
        conexao.commit()

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
        checar = f"SELECT {col_return} FROM {table} WHERE ({col} == {info});"
    else:
        checar = f"SELECT {col_return} FROM {table} WHERE ({col} == '{info}');"
    ponte.execute(checar)
    checar = ponte.fetchall()
    if len(checar) != 0:
        return checar[0][0]
    return False

        
def interface_gerente(info):
    print("Gerente")
    # Supervisiona Vendedores e Abastece estoque
    # Terá lista de vendedores(que ele supervisiona) em que ele pode acessar as vendas de cada um
    

def interface_vendedor(info):
    print("Vendedor")
    # Vendas para efetivar
    # pode acessar suas prórias vendas (pedidos que efetivou)
    
def interface_carrinho(ID):
    print("\n\n---------------------- CARRINHO ----------------------\n")
    carrinho_escolha = int(input("\n 1. Remover Item\n 2. Fechar Pedido\n 3. Ver Carrinho \n 4. Sair do Carrinho \n ---> Insira uma opção: "))
    while carrinho_escolha != 4:
        if carrinho_escolha == 1:
            # LISTAR CARRINHO
            # REMOVER ITEM
            pass
        elif carrinho_escolha == 2:
            all_pedido_id = lista_pedidos()
            new_pedido_id = random.randint(1000, 100000000) not in all_pedido_id # Gera um id para o pedido
        elif carrinho_escolha == 3:
            #listar_carrinho(ID)
            pass
        elif carrinho_escolha != 4:
            print("\n ----- OPÇÃO INVÁLIDA, TENTE NOVAMENTE ------- \n")
        carrinho_escolha = int(input("\n 1. Remover Item\n 2. Fechar Pedido\n 3. Ver Carrinho \n 4. Sair do Carrinho"))
    print("\n --------- Saindo do Carrinho... ---------\n")

def listar_item():
    pesquisar = f"SELECT categoria, cor, item_preco FROM item;"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    return(pesquisa)

def lista_pedidos():
    pesquisar = f"SELECT pedido_id FROM pedido;"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    return(pesquisa[:][0])

def desconto():
    descontar = "SELECT pedido.valor_total FROM pedido WHERE EXISTS ( SELECT is_flamengo, is_op, is_souza FROM cliente WHERE cliente.cliente_id == pedido.clienteFK AND is_flamengo == True OR is_op == True OR is_souza == True)"
    ponte.execute(descontar)
    print("Desconto")
    descontostotais = ponte.fetchall()
    print(descontostotais)
    conexao.commit()

def inserir_cliente(info):
    inserir = "INSERT INTO cliente(nome, username, senha, email, cpf, is_flamengo, is_op, is_souza) VALUES(?,?,?,?,?,?,?,?)"
    ponte.execute(inserir, info)
    conexao.commit()

def inserir_item(info):
    inserir = "INSERT INTO item (item_id, item_preco, lugar_fabricacao, categoria, cor) VALUES(?,?,?,?,?,?,?,?)"
    ponte.execute(inserir, info)
    conexao.commit()

def alterar_item(coluna, novo, chave):
    alterar = f"UPDATE item SET {coluna} = '{novo}' WHERE (item_id == '{chave}');"
    ponte.execute(alterar)
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
    pesquisa = ponte.fetchone()
    print(pesquisa)
    return(pesquisa)

def exibir_um(chave):
    pesquisar = f"SELECT * FROM cliente WHERE (username == '{chave}');"
    ponte.execute(pesquisar)
    pesquisa = ponte.fetchall()
    print(pesquisa)
    return(pesquisa)