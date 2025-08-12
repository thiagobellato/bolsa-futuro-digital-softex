# Listas
vendas = [100, 50, 15, 20, 30, 500, 150]
print(vendas)

# # soma elemnetos da lista
totalVendas = sum(vendas)
print(totalVendas)

# # tamanho da lista
quantidadeVendas = len(vendas)
print(quantidadeVendas)

# # maximo e minimo
print(max(vendas))
print(min(vendas))

# # pegar uma posição da lista
print(vendas[-1])

# verificar um elemneto da lista
listaProdutos = ["iphone", "airpod", "macbook", "ipad" , "apple watch"]

# adicionar item da lista
listaProdutos.append("zulu")

produtoProcurado = input("Pesquise o nome do Produto: ")
print(produtoProcurado in listaProdutos)


temEmEstoque = produtoProcurado in listaProdutos
if temEmEstoque == True:
    print("Temos esse Produto")
else:
    print("Não Temos esse produto")


# # remover item da lista
listaProdutos.remove("apple watch")
listaProdutos.pop(0)


# # editar um item na lista
precoProduto = [1000, 500, 2500, 1500]
precoProduto[0] = precoProduto[0] * 1.5
print(precoProduto)

# #contar quantas vezes um item aparece na lista
listaProdutos = ["iphone", "airpod", "airpod", "iphone", "ipad", "ipad", "ipad"]
print(listaProdutos.count("ipad"))

# ordenar uma lista
listaProdutos.sort()  # ordem alfabética
print(listaProdutos)

listaProdutos.reverse()  # ordem reversa
print(listaProdutos)

precoProduto.sort()
print(precoProduto)

precoProduto.reverse()
print(precoProduto)
