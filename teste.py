from bdinit import *
"""
with conexao:
        ponte = conexao.cursor()
        deletar = "DROP TABLE {cliente,endereco}"
        ponte.execute(deletar)
        conexao.commit()
"""
#create_table()

print("\n LOGIN FUNCIONÁRIO: \n")
email = 'super_gerente@hotmail.com'
senha = '123'
id_func = login_funcionario(email,senha)
if id_func != False:
    print("\n Login do funcionario feito com sucesso \n")
    if check_info('cod_func', id_func, 'cod_func', 'gerente') != False:
        interface_gerente(id_func)
    else:
        interface_vendedor(id_func)
else:
    print("\n Informações incorretas \n")