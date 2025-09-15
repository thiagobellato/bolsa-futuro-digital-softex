from selenium import webdriver
import time
navegador = webdriver.Chrome()
navegador.get("https://ge.globo.com")
navegador.maximize_window()

botao_menu = navegador.find_element("class name", "menu-button")
botao_menu.click()

# time.sleep(10)