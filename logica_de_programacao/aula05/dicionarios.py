dic_produtos = {
    "airpod": [2000, 0],
    "ipad": [9000, 0],
    "iphone": [6000, 256],
    "macbook": [9000, 1000],
}
print(dic_produtos)

# Remove o item "airpod" do dicionário.
dic_produtos.pop("airpod")
print(f"Dicionário após remover o AirPod: {dic_produtos}")

# Adicionar um Produto
dic_produtos["iphone 16"] = 10000

print(f"Preço atual do iPad: {dic_produtos['ipad']}")

# Edita o preço do iPad, aumentando-o em 30%.
dic_produtos["ipad"] = dic_produtos["ipad"] * 1.3
print(f"Preço do iPad após o aumento de 30%: {dic_produtos['ipad']:.2f}")

print(f"Dicionário final: {dic_produtos}")

if "iphone" in dic_produtos:
    print("Existe o Produto")
else:
    print("Produto não existe")

if 9000 in dic_produtos.values():
    print("Existe")
else:
    print("Não existe")
