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