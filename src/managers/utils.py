from datetime import datetime
import os


def get_file_name() -> str:
    """
    Gera um nome de arquivo baseado na data e hora atuais.

    O nome do arquivo é formatado como
    'ARQUIVO_PEDIDOS_DD-MM-YYYY_HH.MM.SS.csv', onde 'DD-MM-YYYY'
    é a data atual e 'HH.MM.SS' é a hora atual.

    Returns:
        str: O nome do arquivo gerado.
    """
    date = datetime.now().strftime('%d-%m-%Y_%H.%M.%S')
    file_name = f'ARQUIVO_PEDIDOS_{date}.csv'
    return file_name


def get_img_name(directory: str, name: str) -> str:
    """
    Gera um caminho completo para um arquivo de imagem baseado
    na data e hora atuais.

    O nome do arquivo é formatado como 'name_DD-MM-YYYY_HH.MM.SS.png',
    onde 'name' é o nome fornecido como argumento, 'DD-MM-YYYY' é a
    data atual e 'HH.MM.SS' é a hora atual. O caminho da imagem
    é construído utilizando o diretório especificado.

    Args:
        directory (str): O diretório onde a imagem será salva.
        name (str): O nome base para o arquivo de imagem.

    Returns:
        str: O caminho completo do arquivo de imagem gerado.
    """
    date = datetime.now().strftime('%d-%m-%Y_%H.%M.%S')
    file_name = f'{name}_{date}.png'
    path_img = os.path.join(directory, file_name)
    return path_img