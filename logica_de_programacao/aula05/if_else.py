vendas_vendedor = float(input("Digite o valor das vendas do vendedor:"))
print(vendas_vendedor)
vendas_empresa = float(input("Digite o valor das vendas da empresa:"))
print(vendas_empresa)
meta_empresa = float(input("Digite o valor da meta da empresa:"))
print(vendas_empresa)
meta1 = float(input("Digite o valor da 1ª meta:"))
print(meta1)
meta2 = float(input("Digite o valor da 2ª meta:"))
print(meta2)
meta3 = float(input("Digite o valor da 3ª meta:"))
print(meta3)

if vendas_vendedor > meta1 and vendas_empresa > meta_empresa:
    print("Meta atingida!!! Bônus Liberado")
    bonus = vendas_vendedor * 0.15
    print(f"Bônus do vendedor: {bonus}")
elif vendas_vendedor > meta2 and vendas_empresa > meta_empresa:
    print("Meta atingida!!! Bônus Liberado")
    bonus = vendas_vendedor * 0.13
    print(f"Bônus do vendedor: {bonus}")
elif vendas_vendedor > meta3 and vendas_empresa > meta_empresa:
    print("Meta atingida!!! Bônus Liberado")
    bonus = vendas_vendedor * 0.1
    print(f"Bônus do vendedor: {bonus}")
else:
    print("Meta não atingida!! Bônus Bloqueado")

lista_produtos = ["iphone", "ipad", "airpod,", "macbook"]
produto_procurado = input("Procure um produto: ").lower()

if produto_procurado in lista_produtos:
    print("Produto em estoque")
else:
    print("Produto não encontrado")


# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# == igual
# != diferente
