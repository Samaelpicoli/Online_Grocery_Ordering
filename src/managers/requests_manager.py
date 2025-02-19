import os
import requests


class RequestManager:
    """
    Classe que gerencia requisições HTTP utilizando a biblioteca requests.

    Essa classe permite realizar requisições GET para URLs, facilitando o
    scraping de dados e a conversão de respostas em arquivos, como CSV.
    
    Utiliza sessões para otimizar múltiplas requisições.

    Attributes:
        session (requests.Session): A sessão HTTP que mantém conexões
        persistentes.
    """

    def __init__(self):
        """
        Inicializa a classe RequestManager.

        Cria uma nova sessão requests para gerenciar as requisições HTTP.
        """
        self.session = requests.Session()

    
    def get_request(self, url: str) -> requests.Response:
        """
        Realiza uma requisição GET para a URL especificada.

        Utiliza a sessão para enviar a requisição, permitindo
        redirecionamentos.

        Args:
            url (str): A URL para a qual a requisição GET será enviada.

        Returns:
            requests.Response: O objeto de resposta da requisição.
        """
        response = self.session.get(url, allow_redirects=True)
        return response
    

    def convert_response_to_file(
            self, response: requests.Response, directory: str, file_name: str
        ) -> str:
        """
        Converte a resposta de uma requisição em um arquivo.

        Verifica se o tipo de conteúdo da resposta é 'text/csv' e, em caso
        afirmativo, salva o conteúdo em um arquivo no diretório especificado.

        Args:
            response (requests.Response): A resposta obtida da requisição.
            directory (str): O diretório onde o arquivo será salvo.
            file_name (str): O nome do arquivo a ser criado.

        Returns:
            str: O caminho completo do arquivo salvo.

        Raises:
            ValueError: Se a resposta não for do tipo CSV.
            Exception: Em caso de erro durante a escrita do arquivo.
        """
        try:
            if 'Content-Type' in response.headers and response.headers[
                'Content-Type'
            ] != 'text/csv':
                raise ValueError("A resposta não é um arquivo CSV.")
            
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return file_path
        except Exception as error:
            raise Exception(f'Erro durante a conversão para arquivo: {error}')