def calcular_imposto(preco):

    if preco <= 2000:
        imposto_renda = 0.2 * preco
    else:
        imposto_renda = 0.3 * preco
        iss = 0.15 * preco
        csll = 0.05 * preco

        imposto_total = imposto_renda + iss + csll
        return imposto_total
        

lista_precos = [3000, 5000, 6000, 7000]

for preco in lista_precos:
    imposto_total = calcular_imposto(preco)
    print(f"Imposto total sobre o produto de R$ {preco}, é de {imposto_total} ")
