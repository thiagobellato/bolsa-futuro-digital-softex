from datetime import date

print("Projeto de Tipos + If e Else ")

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
nota1 = float(input("Digite a nota do 1º Trimestre: "))
nota2 = float(input("Digite a nota do 2º Trimestre: "))
nota3 = float(input("Digite a nota do 3º Trimestre: "))
data = date.today()

notaFinal = (nota1 + nota2 + nota3) / 3

print(f"Olá, {nome}!" f" Sua nota final foi: {notaFinal}")
print(data)

if notaFinal < 5:
    print("Situação: Reprovado")
elif notaFinal >= 5 and notaFinal < 7:
    print("Situação: Aprovado no Curso")
else:
    print("Situação: Aprovado para a Residência")

if idade < 18:
    print(f"Sua idade é: {idade}!! Você é Menor de Idade")
else:
    print(f"Sua idade é: {idade}!! Você é Maior de Idade")
