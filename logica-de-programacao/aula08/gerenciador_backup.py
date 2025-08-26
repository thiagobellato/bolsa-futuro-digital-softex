import os
import tkinter
from tkinter.filedialog import askdirectory
import shutil

nome_pasta_selecionada = askdirectory()
print(nome_pasta_selecionada)

lista_arquivos = os.listdir(nome_pasta_selecionada)
print(lista_arquivos)

nome_pasta_backup = "backup"
nome_completo_pasta_backup = f"{nome_pasta_selecionada}/{nome_pasta_backup}"
if not os.path.exists(nome_completo_pasta_backup):
    os.mkdir(nome_completo_pasta_backup)

for arquivo in lista_arquivos:
    print(arquivo)
    nome_completo_arquivo = f"{nome_pasta_selecionada}/{arquivo}"
    nome_final_arquivo = f"{nome_completo_pasta_backup}/{arquivo}"
    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
    elif "backup" != arquivo:
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)
