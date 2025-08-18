lista_cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Petrópolis",
    "Belo Horizonte",
    "Curitiba",
    "Porto Alegre",
]
print(lista_cidades)

cidade_procurada = input("Digite o nome de uma cidade: ")
print(cidade_procurada in lista_cidades)

print(f"A cidade que você digitou foi {cidade_procurada.lower()}")

# tem_em_estoque = produto_procurado in lista_produtos
# if tem_em_estoque == True:
#     print("Temos esse Produto")
# else:
#     print("Não Temos esse produto")
