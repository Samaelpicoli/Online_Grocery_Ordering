#BIBLIOTECAS UTILIZADAS NO PROCESSO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import os

#MÓDULO UTILIZADO NO PROCESSO
import processo

estado = 'INITIALIZATION'
status_loop = 'ON'

while status_loop == 'ON':
    match estado:
        case 'INITIALIZATION':
            try:
                pasta_destino = os.path.dirname(__file__)
                options = webdriver.ChromeOptions()
                options.add_argument("--disable-notifications")
                options.add_experimental_option("prefs", { "download.default_directory": pasta_destino})
                driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
                wdw = WebDriverWait(driver, 40)
                processo.inicia_site(driver, wdw)
                estado = 'GET TRANSACTION'
                continue
            except Exception as error:
                print('Erro durante a inicialização: ' + error)
                state = 'END'
                continue
        
        case 'GET TRANSACTION':
            try:
                arquivo = processo.extrai_dados(pasta_destino)
                estado = 'PROCESS'
                continue
            except Exception as error:
                print('Erro durante a captura dos dados: ' + error)
                estado = 'END'
                continue

        case 'PROCESS':
            try:              
                processo.insere_dados(driver, arquivo)
                processo.captura_tempo(driver, wdw)
                estado = 'END'
                continue
            except Exception as error:
                print('Erro durante o processamento: ' + error)
                estado = 'END'
                continue

        case 'END':
            driver.close()
            driver.quit()
            status_loop = 'OFF'
            continue

