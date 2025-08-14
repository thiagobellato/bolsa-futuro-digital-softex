from datetime import date
from sys import exit

print("Projeto de Tipos + If e Else ")

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))


if idade < 18:
    print("Acesso Negado!!! Você precisa ser maior de idade para continuar.")
    exit()
else:
    print("Acesso Liberado!! Você é maior de idade")

nota_1 = float(input("Digite a nota do 1º Trimestre: "))
nota_2 = float(input("Digite a nota do 2º Trimestre: "))
nota_3 = float(input("Digite a nota do 3º Trimestre: "))
data = date.today()

nota_final = (nota_1 + nota_2 + nota_3) / 3

print(f"Olá, {nome.capitalize()}!" f" Sua nota final foi: {nota_final}")
print(data)

if nota_final < 5:
    print("Situação: Reprovado")
elif nota_final >= 5 and nota_final < 7:
    print("Situação: Aprovado no Curso")
else:
    print("Situação: Aprovado para a Residência")
