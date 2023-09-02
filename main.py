#BIBLIOTECAS UTILIZADAS NO PROCESSO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time
import os
import getpass

#MÓDULO UTILIZADO NO PROCESSO
import processo


user = getpass.getuser()
pasta_destino = f'C:\\Users\\{user}\\Downloads'
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_experimental_option("prefs", { "download.default_directory": pasta_destino})
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
wdw = WebDriverWait(driver, 40)


processo.inicia_site(driver, wdw)
arq = processo.extrai_dados(pasta_destino)
processo.insere_dados(driver, arq)
processo.captura_tempo(driver, wdw)

print('Atividade realizada com sucesso!')
driver.close()
driver.quit()

