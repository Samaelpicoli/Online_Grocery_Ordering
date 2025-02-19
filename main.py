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
            """
            Estado de inicialização do processo.

            Neste estado, a aplicação configura o ambiente de execução,
            incluindo a inicialização do logger, a configuração do WebDriver
            e a realização do login no site. Este estado também combina o
            uso de Selenium para automação de navegador e Requests para
            manipulação de requisições HTTP.

            O fluxo de controle é gerenciado aqui, onde as classes interagem
            para realizar operações de login e captura de dados. As interações
            entre as classes são centralizadas no método principal, garantindo
            uma arquitetura clara e modular.

            Attributes:
                logger (Logger): Instância do logger para registrar 
                informações.
                options (WebDriverOptions): Configurações do WebDriver.
                login_page (PageLogin): Classe responsável pelas interações
                na página De login.
                main_page (PageMain): Classe responsável pelas interações na
                página principal.
                request_manager (RequestManager): Classe para gerenciar
                requisições HTTP.
                excel_file (CsvManager): Classe para manipulação de
                arquivos CSV.
            """
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
            """
            Estado para captura e processamento de transações.

            Neste estado, a aplicação lê uma planilha (arquivo Excel) e
            captura o item correspondente ao ID da transação atual.
            O uso do ID para acessar diretamente linhas específicas da
            planilha otimiza as consultas e permite um processamento
            mais eficiente das transações.

            A leitura sequencial por ID também facilita a implementação
            de paralelismo, uma vez que diferentes threads ou processos
            podem operar sobre diferentes IDs simultaneamente, aumentando
            a eficiência e reduzindo o tempo total de execução.

            O fluxo é o seguinte:
                1. Salva o arquivo Excel atualizado.
                2. Incrementa o ID da transação para capturar a próxima linha.
                3. Registra a ação para fins de rastreamento.
            """
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
            """
            Estado para processamento de transações.

            Neste estado, a aplicação manipula a ordem de alimentos a
            partir do item capturado anteriormente. A lógica de processamento
            está preparada para suportar paralelismo, permitindo que múltiplas
            instâncias do processo operem simultaneamente em diferentes
            transações.

            O fluxo de trabalho inclui:
                1. Verificação do status do item. Se 'pendente', inicia o
                processamento.
                2. Atualização do status no arquivo Excel para 'Processando'.
                3. Inserção da ordem de comida utilizando a classe `PageMain`.
                4. Atualização do status no arquivo Excel para 'Sucesso'
                após a inserção.
                5. Tratativas de erro: caso ocorra uma exceção, o status
                é atualizado para 'Falha', e uma captura de tela é feita para
                documentação do erro.

            A comunicação entre as classes `PageMain` e `CsvManager` é
            essencial, permitindo que a aplicação mantenha o estado dos dados
            enquanto interagE com a interface do usuário. Os logs são
            utilizados para registrar informações importantes sobre o fluxo e
            facilitar a depuração em caso de falhas.
            """
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
            """
            Estado de finalização do processo.

            Neste estado, a aplicação realiza as operações finais
            após o processamento das transações. As principais atividades
            incluem:

                1. Submissão do pedido utilizando a classe `PageMain`, que
                interage com a interface do usuário para completar a transação.
                2. Captura do tempo e da acurácia do processamento, permitindo
                a análise da eficiência do sistema.
                3. Geração de uma captura de tela de sucesso para documentação,
                que fornece um registro visual do resultado final.
                4. Fechamento do driver do Selenium, garantindo que todos os
                recursos sejam liberados corretamente após a execução.
                5. Movimentação do arquivo processado para o diretório de
                destino, organizando os dados de forma que possam ser
                facilmente acessados posteriormente.
                6. Registro de informações no log sobre o tempo de
                processamento e a acurácia do preenchimento, contribuindo
                para um melhor entendimento do desempenho do sistema.

            Esse estado marca a conclusão do ciclo de processamento, e todas
            as informações relevantes são registradas para futuras
            referências.
            """
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



        

            

