try:
    numero1 = int(input("Digite o 1º número:"))
    numero2 = int(input("Digite o 2º número:"))
    numero3 = int(input("Digite o 3º número:"))
    print(f"Os números digitados foram: \n{numero1}\n{numero2}\n{numero3}")
except ValueError:
    print("Entrada inválida!! Por favor, digite apenas números")
