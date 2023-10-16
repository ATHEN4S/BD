
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


UNIQUE (cpf),
UNIQUE (username),
CONSTRAINT ck_nome CHECK (length(nome) < 50 and length(nome) >= 3 )
CONSTRAINT ck_username CHECK (length(username)< 15 and length(username) >= 3)
CONSTRAINT ck_senha CHECK (length(senha)>4 and length(senha)<15),
CONSTRAINT ck_cpf CHECK (length(cpf)== 11)
CONSTRAINT ck_email CHECK (Email LIKE '%_@_%._%')
);
"""
        ponte.execute(create)
        conexao.commit()


def inserir_cliente(info):
    with conexao:
        ponte = conexao.cursor()

        inserir = "INSERT INTO cliente(nome, username, senha, email, cpf) VALUES(?,?,?,?,?)"
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