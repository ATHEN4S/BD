from bdinit import *

with conexao:
        ponte = conexao.cursor()
        deletar = """DROP TABLE cliente;
                    DROP TABLE endereco;
                    DROP TABLE item;
                    DROP TABLE pedido;
                    DROP TABLE carrinho;
                    DROP TABLE estoque;
                    DROP TABLE funcionario;
                    DROP TABLE vendedor;
                    DROP TABLE gerente;"""
        
        ponte.executescript(deletar)
        conexao.commit()

create_table()
"""
inserir = "INSERT INTO pedido(pedido_id, qtd_itens, valor_total, pagamento, status_pagamento, clienteFK) VALUES(?,?,?,?,?,?)"
ponte.execute(inserir, [31234, 1, 10, 'Crédito', 'Em_andamento', 1])
conexao.commit()

pesquisar = f"SELECT pedido_id FROM pedido;"
ponte.execute(pesquisar)
pesquisa = ponte.fetchall()
for pedido in pesquisa[:][0]:
        print(pedido)
"""
while True:
        try:
                add_carrinho = int(input("\n Digite o ID(INTEIRO) do item que deseja adicionar ao carrinho: \n -----> "))
        except ValueError:
                print("ERRO: NÃO FOI DIGITADO UM NÚMERO INTEIRO ")
        
        #carrinho = listar_carrinho()
        ask = input("Digite se você deseja continuar (s/n):\n ----> ")
        while ask != 's' and ask != 'n':
                ask = input("Digite se você deseja continuar (s/n):\n ----> ")
        if ask == 'n':
                break