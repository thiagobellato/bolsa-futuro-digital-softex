import os

# import datetime
# import pyautogui

# print(os.listdir("../arquivos"))
# agora = datetime.datetime.now()
# data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
# print(f"Data e hora formatadas: {data_formatada}")

# pyautogui.press("win")
# pyautogui.write("vscode")

lista_arquivos = os.listdir("arquivos")
print(lista_arquivos)

for arquivo in lista_arquivos:
    if "txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
            print("Movimentar para a pasta 22", arquivo)
        elif "23" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")
            print("Movimentar para a pasta 23", arquivo)
