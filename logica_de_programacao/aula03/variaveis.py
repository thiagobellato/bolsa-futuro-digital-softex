faturamento = 1500  # variavel int
print(faturamento)
custo = 1700
print(custo)  # variavel float
novas_vendas = 100
print(novas_vendas)
imposto = 0.10
print(imposto)
faturamento += novas_vendas
print(faturamento)
lucro = faturamento - (faturamento * imposto) - custo
print(lucro)
margem_lucro = lucro / faturamento
print(f"{margem_lucro:.3f}%")

nome = "Thiago"  # variavel string
email = "tfbellato@hotmail.com"  # variavel string

teve_lucro = True  # variavel boolean
if faturamento > custo:
    teve_lucro = True
    print("A empresa teve lucro")
elif faturamento == custo:
    teve_lucro = False
    print("A empresa não teve lucro")
else:
    faturamento < custo
    teve_lucro = False
    print("A empresa teve prejuízo")

print(
    f"O Faturamento foi de R${faturamento:.2f}\n"
    f"Os custos foram de R${custo:.2f}\n"
    f"O lucro final foi de R${lucro:.2f}\n"
    f"A carga tributária foi de {imposto:.2f}%\n"
    f"A margem de lucro foi de {margem_lucro:.3f}%\n"
    f"Lucro: {teve_lucro}\n"
)

# # # int ("Números Inteiros")
# # # float ("Números Reais")
# # # complex
# # # str("Texto")
# # # list
# # # tuple
# # # range
# # # dict
# # # set
# # # frozenset
# # # bool("True e False")
# # # bytes
# # # bytearray
# # # memoryview
