email = input("Digite o seu e-mail: ")
nome = input("Digite o seu nome: ")

print(nome, email)
print (f"{nome}, verifique seu e-mail: {email} para confirmar o seu cadastro")


faturamento = float(input(f"Digite o seu faturamento: "))
imposto = float(input(f"Digite a taxa de imposto: "))

imposto = faturamento * imposto

print(faturamento)
print(imposto)


lucro = faturamento - imposto
print(lucro)

