# Listas
vendas = [100, 50, 15, 20, 30, 500, 150]
print(vendas)

# # soma elemnetos da lista
total_vendas = sum(vendas)
print(total_vendas)

# # tamanho da lista
quantidade_vendas = len(vendas)
print(quantidade_vendas)

# # maximo e minimo
print(max(vendas))
print(min(vendas))

# # pegar uma posição da lista
print(vendas[-1])

# verificar um elemneto da lista
lista_produtos = ["iphone", "airpod", "macbook", "ipad", "apple watch"]

# adicionar item da lista
lista_produtos.append("zulu")

produto_procurado = input("Pesquise o nome do Produto: ")
print(produto_procurado in lista_produtos)


tem_em_estoque = produto_procurado in lista_produtos
if tem_em_estoque == True:
    print("Temos esse Produto")
else:
    print("Não Temos esse produto")


# # remover item da lista
lista_produtos.remove("apple watch")
lista_produtos.pop(0)


# # editar um item na lista
preco_produto = [1000, 500, 2500, 1500]
preco_produto[0] = preco_produto[0] * 1.5
print(preco_produto)

# #contar quantas vezes um item aparece na lista
lista_produtos = ["iphone", "airpod", "airpod", "iphone", "ipad", "ipad", "ipad"]
print(lista_produtos.count("ipad"))

# ordenar uma lista
lista_produtos.sort()  # ordem alfabética
print(lista_produtos)

lista_produtos.reverse()  # ordem reversa
print(lista_produtos)

preco_produto.sort()
print(preco_produto)

preco_produto.reverse()
print(preco_produto)
