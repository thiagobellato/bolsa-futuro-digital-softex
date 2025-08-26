import os
import tkinter
from tkinter.filedialog import askdirectory
import shutil

nome_pasta_selecionada = askdirectory()
print(nome_pasta_selecionada)

lsita_arquivos = os.listdir(nome_pasta_selecionada)
print(lsita_arquivos)