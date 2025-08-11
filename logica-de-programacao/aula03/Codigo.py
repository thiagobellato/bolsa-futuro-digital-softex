# faturamento = 1500 #variavel int
# custo = 750.25 #variavel float
# novasVendas = 100
# imposto = faturamento * 0.1
# print (faturamento - imposto)
# faturamento += novasVendas
# print (faturamento)
# imposto = faturamento * 0.14
# lucro = faturamento - custo - imposto
# margemLucro = lucro/faturamento

# nome = 'Thiago' #variavel string
# email = 'tfbellato@hotmail.com' #variavel string
# teveLucro = True #variavel boolean
# pi = 3.14159265

# print(f"O Faturamento foi de R${faturamento:.2f}")
# print(f"Os custos foram de R${custo:.2f}")
# print(f"O lucro final foi de R${lucro:.2f}")
# print(f"A carga tributária foi de R${imposto:.2f}")
# print(f"A margem de lucro foi de {margemLucro:.2f}")

# #mod = sobra da divisão

# tempoContrato = 170
# tempoAnos = tempoContrato / 12
# print("Tempo em anos",int(tempoAnos))
# tempoMeses = (tempoContrato % 12)
# print(f"Tempo em meses {tempoMeses}")

# faturamento = 1000
# custo = 700
# lucro = faturamento - custo

# print(f"Faturamento da empresa: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}")
nomeCliente = "João"
emailCliente = "joao@Gmail.cOm"

print(emailCliente)

#manipulação de str (maiusculo)
emailCliente = emailCliente.upper()
print(emailCliente)

#manipulação de str (minusculo)
emailCliente = emailCliente.lower()
print(emailCliente)

#find
print(emailCliente.find("@"))#-1 quando não encontrado

#tamanho
print(len(emailCliente))
print(len(nomeCliente))

#buscar
print((emailCliente[0]))
print((nomeCliente[0]))


# # print(f"{pi:.2f}")
# # int ("Números Inteiros")
# # float ("Números Reais")
# # complex
# # str("Texto")
# # list
# # tuple
# # range
# # dict
# # set
# # frozenset
# # bool("True e False")
# # bytes
# # bytearray
# # memoryview