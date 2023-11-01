
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
is_OP BOOL NOT NULL DEFAULT FALSE,
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
clienteFK integer NOT NULL,
FOREIGN KEY(clienteFK) REFERENCES cliente(cliente_id)
ON DELETE SET NULL
ON UPDATE CASCADE
);

CREATE TABLE itens_pedido(
pedido_id integer PRIMARY KEY NOT NULL,
qtd_item integer NOT NULL,
item_idFK integer NOT NULL,
FOREIGN KEY(item_idFK) REFERENCES item(item_id)
ON DELETE SET NULL
ON UPDATE CASCADE
);

CREATE TABLE estoque(
item_id integer PRIMARY KEY NOT NULL,
qtd_estoque integer NOT NULL DEFAULT 0
);

CREATE TABLE funcionario(
cod_func integer PRIMARY KEY NOT NULL,
nome VarChar(30) NOT NULL,
senha VarChar(15) NOT NULL,
email VarChar(50) NOT NULL,
cpf VarChar(20) NOT NULL
CONSTRAINT email CHECK (email LIKE '%_@_%._%')
CONSTRAINT senha CHECK (length(senha) < 15 and length(senha) >= 3 )
);

CREATE TABLE vendedor(
cod_func integer PRIMARY KEY NOT NULL,
conf_venda VarChar(50) NOT NULL DEFAULT 0,
pedido_idFK integer NOT NULL,
FOREIGN KEY(pedido_idFK) REFERENCES pedido(pedido_id)
ON UPDATE CASCADE
ON DELETE SET NULL
);

CREATE TABLE gerente(
cod_func PRIMARY KEY NOT NULL,
vendedorFK integer,
FOREIGN KEY(vendedorFK) REFERENCES vendedor(cod_func)
ON UPDATE CASCADE
ON DELETE SET NULL
);

INSERT INTO funcionario(cod_func, nome, senha, email, cpf)
VALUES(1, 'First', '123', 'super_gerente@hotmail.com', '00000000001');
INSERT INTO gerente(cod_func, vendedorFK)
VALUES(1, NULL)
;
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
    if check_info('user', user, 'cliente_id','cliente') != False and check_info('senha', senha, 'cliente_id', 'cliente') != False:
        return check_info('user', user, 'cliente_id','cliente')
    return False

def check_info(col, info, col_return, table):
    """
    with conexao:
        ponte = conexao.cursor()
        checar = f"SELECT {col_return} FROM {table} WHERE ({col} == '{info}');"
        ponte.execute(checar)
        checar = ponte.fetchall()
        if len(checar) != 0:
            return checar # retorno: [(1,)], mas queria que retornasse só o 1
        return False
    """
    with conexao:
        ponte = conexao.cursor()
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
    print(info)

def interface_vendedor(info):
    print("Vendedor")
    # Vendas para efetivar
    # pode acessar suas prórias vendas (pedidos que efetivou)
    print(info)

def inserir_cliente(info):
    with conexao:
        ponte = conexao.cursor()

        inserir = "INSERT INTO cliente(nome, username, senha, email, cpf, is_flamengo, is_OP, is_souza) VALUES(?,?,?,?,?,?,?,?)"
        ponte.execute(inserir, info)
        conexao.commit()


def alterar_cliente(coluna, novo, chave):
    with conexao:
        ponte = conexao.cursor()
        alterar = f"UPDATE cliente SET {coluna} = '{novo}' WHERE (username == '{chave}');"
        ponte.execute(alterar)
        conexao.commit()

def pesquisar_nome(chave):
    with conexao:
        ponte = conexao.cursor()
        pesquisar = f"SELECT * FROM cliente WHERE (nome LIKE '{chave}');"
        ponte.execute(pesquisar)
        pesquisa = ponte.fetchall()
        print(pesquisa)
        return(pesquisa)

def remover_cliente(info):
    with conexao:
        ponte = conexao.cursor()
        deletar = f"DELETE FROM cliente WHERE (username = '{info}');"
        ponte.execute(deletar)
        conexao.commit()

def listar_todos():
    with conexao:
        ponte = conexao.cursor()
        pesquisar = f"SELECT * FROM cliente;"
        ponte.execute(pesquisar)
        pesquisa = ponte.fetchall()
        return(pesquisa)
    
def exibir_um(chave):
    with conexao:
        ponte = conexao.cursor()
        pesquisar = f"SELECT * FROM cliente WHERE (username == '{chave}');"
        ponte.execute(pesquisar)
        pesquisa = ponte.fetchall()
        print(pesquisa)
        return(pesquisa)