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

#create_table()

#vendedor_gerente(2)
"""
inserir = "INSERT INTO carrinho(qtd_item, item_idFK, clienteFK) VALUES(?,?,?)"
ponte.execute(inserir, [2, 1479, 1])
conexao.commit()
inserir = "INSERT INTO carrinho(qtd_item, item_idFK, clienteFK) VALUES(?,?,?)"
ponte.execute(inserir, [3, 2324, 1])
conexao.commit()

inserir = "INSERT INTO pedido(pedido_id, qtd_itens, valor_total, pagamento, status_pagamento, status, mes, clienteFK) VALUES(?,?,?,?,?,?,?,?)"
ponte.execute(inserir, [31234, 5, 10, 'Crédito', 'Em_andamento', 'Não Confirmado','1', 1])
conexao.commit()
pedido_carrinho = f"UPDATE carrinho SET pedidoFK = 31234 WHERE clienteFK = 1"
ponte.execute(pedido_carrinho)
conexao.commit()

# EXEMPLO DE VIEW
item_id = 1479
pesquisar = f"CREATE TEMPORARY VIEW view_name AS
SELECT * FROM item I INNER JOIN estoque E ON item_id = item_idFK WHERE item_idFK = {item_id};"
ponte.execute(pesquisar)
pesquisa = ponte.fetchall()


pesquisar = "SELECT* FROM view_name"
ponte.execute(pesquisar)
pesquisa = ponte.fetchall()
print(pesquisa)
pesquisar = "SELECT qtd_estoque FROM view_name"
ponte.execute(pesquisar)
pesquisa = ponte.fetchall()
print(pesquisa)
"""