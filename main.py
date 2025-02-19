from config import *

from src.pom.pages.page_login import PageLogin
from src.pom.pages.page_main import PageMain
from src.managers.csv_manager import CsvManager
from src.managers.directory_manager import DirectoryManager
from src.managers.logger import Logger
from src.managers.requests_manager import RequestManager
from src.managers import utils
from src.managers.web_driver_options import WebDriverOptions

"""
Antes da execução, por favor leia o arquivo README.md para um melhor entendimento.
"""

while loop == 'ON':
    match state:

        case 'INITIALIZATION':
            try:
                if first_execution:

                    logger = Logger()
                    logger.info('Iniciou o Processo.')

                    options = WebDriverOptions()
                    options.add_argument("--disable-notifications")
                    options.add_argument("--start-maximized")

                    first_execution = False

                login_page = PageLogin()
                login_page.open_site(URL)
                login_page.perform_login(EMAIL, SENHA)

                main_page = PageMain()

                logger.info('Login realizado no site.')

                file_name_initial = utils.get_file_name()
                
                directory_saved_file = DirectoryManager(DIRECTORY_SAVED_FILE)
                exist_file = directory_saved_file.get_file(file_name_initial)

                if not exist_file:

                    url = main_page.get_url_file()

                    request_manager = RequestManager()
                    response = request_manager.get_request(url)
                    file = request_manager.convert_response_to_file(
                        response, DIRECTORY_SAVED_FILE, file_name_initial
                    )

                    logger.info(f'Arquivo foi gerado na pasta: {file}')

                    excel_file = CsvManager(file)
                    excel_file.add_column_status()
                    

                state = 'GET TRANSACTION'
                continue

            except Exception as error:
                logger.error(
                    f'Erro durante a inicialização do processo {error}'
                )

                img_path = utils.get_img_name(DIRECTORY_SCREENSHOTS_ERROR, 'erro')
                main_page.screenshot_of_screen(img_path)

                state = 'END'
                continue


        case 'GET TRANSACTION':
            try:
                excel_file.save_file()

                transaction_id = transaction_id+1

                item = excel_file.get_row_by_id(transaction_id)

                logger.info('Captura item para processamento.')

                state = 'PROCESS'
                continue

            except IndexError as error:
                logger.info('Todas as linhas foram executadas.')

                state = 'END'
                continue


        case 'PROCESS':
            try:
                if item['status'] == 'pendente':
                    food_order = item['Favorite Food']

                    logger.info(f'Inserindo no input: {food_order}.')

                    excel_file.update_value_by_id(
                        transaction_id, 'status', 'Processando'
                    )
                    excel_file.save_file()

                    main_page.perform_orderings(food_order)

                    excel_file.update_value_by_id(
                        transaction_id, 'status', 'Sucesso'
                    )

                    logger.info('Item inserido com Sucesso.')

                    state = 'GET TRANSACTION'
                    continue

            except Exception as error:
                excel_file.update_value_by_id(
                    transaction_id, 'status', 'Falha'
                )

                img_path = utils.get_img_name(DIRECTORY_SCREENSHOTS_ERROR, 'erro')
                main_page.screenshot_of_screen(img_path)

                main_page.close_driver()

                logger.error(
                    f'Erro durante o processamento do item {food_order}: {error}'
                )

                state = 'INITIALIZATION'
                continue


        case 'END':
            main_page.perform_submit_ordering()
            time, accuracy = main_page.get_time()

            img_path = utils.get_img_name(DIRECTORY_SCREENSHOTS_SUCCESS, 'SUCCESS')
            main_page.screenshot_of_screen(img_path)

            logger.info(
                f'Tempo de processamento: {time} - Acurácia no prrenchimento: {accuracy}'
            )

            main_page.close_driver()

            file_name_ended = utils.get_file_name()

            directory_destination = DirectoryManager(DIRECTORY_DESTINATION_FILE)
            move_file = directory_saved_file.move_file(
                file, DIRECTORY_DESTINATION_FILE
            )

            logger.info(move_file)
            logger.info('Processo finalizado.')
            loop = 'OFF'
            continue




