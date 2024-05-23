from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import requests
from pathlib import Path

class OnlineGroceryOrdering:

    """
    Classe responsável pela automação de pedidos de compras de 
    supermercado online, incluindo o download de uma lista de compras, 
    inserção de itens em um formulário web e captura tela de
    métricas de desempenho.
    """

    url = '''https://developer.automationanywhere.com/challenges/
    AutomationAnywhereLabs-ShoppingList.html?_fsi=2TeusPzS&_ga=2.127413901.
    1602602311.1693667838-332041422.1681954902&_gl=1*198a2vk*_
    ga*MzMyMDQxNDIyLjE2ODE5NTQ5MDI.*_ga_DG1BTLENXK*MTY5MzY2NzgzNy4yL
    jEuMTY5MzY2Nzg5MC43LjAuMA..'''

    def __init__(self, pasta):
        """
        Inicializa a classe configurando o driver, request
        e preparando os diretórios de trabalho.

        Args:
            pasta (str): Caminho da pasta onde o arquivo csv será salvo.
        """
        self._pasta = Path(pasta)
        self._pasta.mkdir(exist_ok=True)
        self._pasta_screenshot = Path('Captura do Tempo')
        self._pasta_screenshot.mkdir(exist_ok=True)
        self._service = Service(ChromeDriverManager().install())
        self._driver = webdriver.Chrome(service=self._service)
        self._wdw = WebDriverWait(self._driver, 40)
        self._driver.get(OnlineGroceryOrdering.url)
        self._driver.maximize_window()
        self._session = requests.Session()

    def _realizar_request_arquivo(self):
        """
        Realiza uma requisição HTTP para baixar o arquivo CSV contendo a 
        lista de compras.

        Raises:
            Exception: Erros durante a requisição HTTP.

        Returns:
            requests.Response: Resposta HTTP contendo o arquivo.
        """
        try:
            url_arquivo = '''
                https://aai-devportal-media.s3.us-west-2.amazonaws.com/
                challenges/shopping-list.csv'''
            resposta = self._session.get(url_arquivo, allow_redirects=True)
            return resposta
        
        except Exception as error:
            raise Exception(f'Erro durante a realização do Requests: {error}')

    def _criar_arquivo(self):
        """
        Salva o conteúdo do arquivo CSV obtido via HTTP em um arquivo local.

        Raises:
            Exception: Erros que podem ocorrer ao salvar o arquivo.

        Returns:
            str: Caminho do arquivo salvo.
        """
        try:
            requisicao = self._realiza_request_arquivo()
            nome_arquivo = 'shopping-list.csv'
            caminho_arquivo = self._pasta / nome_arquivo
            with open(caminho_arquivo, 'wb') as arquivo:
                arquivo.write(requisicao.content)
            return caminho_arquivo
        except Exception as error:
            raise Exception(f'Erro durante a criação do arquivo: {error}')

    def extrair_dados(self):
        """
        Extrai dados do arquivo CSV e carrega-os em um DataFrame.

        Returns:
            DataFrame: objeto que contém os dados lidos do arquivo CSV.
            None: Em caso de erro na leitura.
        """
        try:
            arquivo = self._criar_arquivo()
            df = pd.read_csv(arquivo, sep=',')
            return df
        except Exception as error:
            print(f'Erro durante a extração dos dados: {error}')
            return None

    def exibir_dados(self, dados):
        """
        Exibe os dados do DataFrame fornecido.

        Args:
            dados (DataFrame): DataFrame contendo os dados do arquivo CSV.
        """
        print(dados)
    
    def inserir_dados(self, dados):
        """
        Insere os itens da lista de compras no formulário web.

        Args:
            dados (DataFrame): DataFrame contendo os dados a serem inseridos.

        Raises:
            Exception: Erro durante a inserção dos dados.
        """
        try:
            for index, linha in dados.iterrows():
                item = linha['Favorite Food']
                self._driver.find_element(By.ID, 'myInput').send_keys(item)
                self._driver.find_element(By.ID, 'add_button').click()

            self._driver.find_element(By.ID, 'agreeToTermsYes').click()
            self._driver.find_element(By.ID, 'submit_button').click()
        
        except Exception as error:
            raise Exception(f'Erro ao inserir os dados: {error}')

    def capturar_tempo(self):
        """
        Captura a tela após a conclusão das inserções e salva o 
        screenshot para referência futura.

        Raises:
            Exception: Erro ao capturar o screenshot da tela.
        """
        try:
            self._wdw.until(ec.element_to_be_clickable
                            ((By.ID, 'download-btn-modal')))
            caminho_screenshot = self._pasta_screenshot / 'acuracia.png'
            self._driver.save_screenshot(caminho_screenshot)
        
        except Exception as error:
            raise Exception(f'Erro ao capturar o tempo de execução: {error}')

    def encerrar_driver(self):
        """
        Encerra o driver do navegador, fechando todas as janelas associadas.
        """
        self._driver.quit()
