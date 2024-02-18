from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pandas as pd

import pega_arquivo as arquivo

def inicia_site(driver, wdw):
    try:
        driver.get('https://developer.automationanywhere.com/challenges/AutomationAnywhereLabs-ShoppingList.html?_fsi=2TeusPzS&_ga=2.127413901.1602602311.1693667838-332041422.1681954902&_gl=1*198a2vk*_ga*MzMyMDQxNDIyLjE2ODE5NTQ5MDI.*_ga_DG1BTLENXK*MTY5MzY2NzgzNy4yLjEuMTY5MzY2Nzg5MC43LjAuMA..')
        driver.maximize_window()
        wdw.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/p/a')))
    except Exception as e:
        print(e)
        raise Exception('Erro ao inicializar o site.')

def extrai_dados(pasta):
    try:
        arq = arquivo.solicitar_csv()
        df = pd.read_csv(f'{pasta}\{arq}', sep=',')
        print(df)
        return df
    except Exception as e:
        print(e)
        raise Exception('Erro ao realizar a leitura de dados do arquivo.')

def insere_dados(driver, df):
    try:
        for index, linha in df.iterrows():
            item = linha['Favorite Food']
            print(item)
            driver.find_element(By.ID, 'myInput').send_keys(item)
            driver.find_element(By.ID, 'add_button').click()

        driver.find_element(By.ID, 'agreeToTermsYes').click()
        driver.find_element(By.ID, 'submit_button').click()
    except Exception as e:
        print(e)
        raise Exception('Erro ao inserir dados no site.')

def captura_tempo(driver, wdw):
    try:
        wdw.until(ec.element_to_be_clickable((By.ID, 'download-btn-modal')))
        driver.save_screenshot('acuracia.png')
    except Exception as e:
        print(e)
        raise Exception('Erro ao capturar dados dentro do modal.')