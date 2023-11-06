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
"""
mes = '12'
hist = f'''CREATE TEMP VIEW RelatorioMensal AS
        SELECT  vendedor.funcFK, vendedor.pedido_idFK,pedido.mes, pedido.qtd_itens, pedido.valor_total
        FROM  vendedor INNER JOIN pedido ON pedido.pedido_id = vendedor.pedido_idFK;
        '''
ponte.execute(hist)
pesquisar = f"SELECT * FROM RelatorioMensal WHERE mes = {mes}"
ponte.execute(pesquisar)
pesquisa = ponte.fetchall()

linha = 0
valor_total = 0
for i in pesquisa:
        print(f"|| Código Funcionário: {pesquisa[linha][0]} || Código Pedido: {pesquisa[linha][1]} || Mês: {pesquisa[linha][2]} || Quantidade Itens: {pesquisa[linha][3]} || Valor Total: {pesquisa[linha][4]}")
        valor_total += pesquisa[linha][4]
        linha += 1
print(f"\nGanho Total: {valor_total}")
print(f"Número de Vendas: {linha}")



#vendedor_gerente(2)

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

CREATE VIEW RelatorioMensal AS
SELECT  vendedor.funcFK, vendedor.pedido_idFK,pedido.mes, pedido.qtd_itens, pedido.valor_total
FROM  vendedor FULL OUTER JOIN pedido ON pedido.pedido_id = vendedor.pedido_idFK WHERE pedido.mes = 11;


"""