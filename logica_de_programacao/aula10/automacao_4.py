from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicia o driver do navegador Chrome
print("Iniciando o navegador...")
driver = webdriver.Chrome()

# Maximiza a janela do navegador para melhor visualização (opcional)
driver.maximize_window()

# Navega até o site do Google
print("Acessando o Google...")
driver.get("https://www.google.com")
time.sleep(2) # Pausa para a página carregar completamente

# --- O que está acontecendo aqui:
# 1. 'find_element(By.NAME, "q")' - Este comando localiza a barra de pesquisa.
#    O Google nomeia o campo de pesquisa como "q", então usamos essa informação.
# 2. '.send_keys("aulas de python")' - Este comando simula a digitação do texto.
# 3. '+ Keys.ENTER' - Adiciona a ação de pressionar a tecla "Enter".

print("Digitando 'aulas de python' e pesquisando...")
barra_de_pesquisa = driver.find_element(By.NAME, "q")
barra_de_pesquisa.send_keys("aulas de python" + Keys.ENTER)

# Pausa de 5 segundos para você ver o resultado da pesquisa
print("Esperando 5 segundos para você ver o resultado...")
time.sleep(5)

# Fecha o navegador
# print("Fechando o navegador.")
# driver.quit()

# print("Automação concluída!")