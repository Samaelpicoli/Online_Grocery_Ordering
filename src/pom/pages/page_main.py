from typing import Tuple
from src.pom.web_driver_base_actions import WebDriverBaseActions
from src.pom.locators.page_main_locators import PageMainLocators


class PageMain(WebDriverBaseActions):
    """Classe para interações na página principal da aplicação web.

    Esta classe utiliza o padrão de design Page Object Model (POM) para
    encapsular a lógica de interação com os elementos da página principal.
    O POM facilita a manutenção do código, permitindo uma separação clara
    entre a lógica de teste e a estrutura da página.

    Attributes:
        driver (WebDriver): A instância do Selenium WebDriver, herdada
        da classe base.
    """

    def __init__(self):
        """
        Inicializa a página principal chamando o construtor da classe base.

        A classe base WebDriverBaseActions fornece métodos comuns para 
        interações com o WebDriver, como clicar em elementos e digitar texto.
        """
        super().__init__()


    def get_url_file(self) -> str:
        """
        Captura o atributo href do botão de download na página.

        Este método utiliza os localizadores definidos na classe 
        PageMainLocators para encontrar o botão de download e obter
        o URL associado.

        Returns:
            str: O URL do arquivo a ser baixado.

        Raises:
            Exception: Se ocorrer um erro ao capturar o atributo href do elemento.
        """
        try:
            attribute = self._find_element_in_page(PageMainLocators.BUTTON_DOWNLOAD)
            href_value = attribute.get_attribute('href')
            return href_value
        except Exception as error:
            raise Exception(
                f'Erro ao capturar o atributo href do elemento: {error}'
            )


    def perform_orderings(self, food: str):
        """
        Realiza o pedido de comida na página.

        Este método interage com os campos de entrada e botões utilizando
        os localizadores definidos na classe PageMainLocators para adicionar
        um item ao pedido.

        Args:
            food (str): O nome da comida a ser adicionada ao pedido.

        Raises:
            Exception: Se ocorrer um erro durante o preenchimento dos pedidos.
        """
        try:
            self._type_input(PageMainLocators.INPUT_ORDER_FOOD, food)
            self._click(PageMainLocators.BUTTON_ADD_ITEM)
        except Exception as error:
            raise Exception(
                f'Erro durante o preenchimento dos pedidos: {error}'
            )


    def perform_submit_ordering(self):
        """
        Finaliza o pedido na página.

        Este método clica na checkbox de termos e no botão de submissão do
        pedido, utilizando os localizadores definidos na classe
        PageMainLocators.

        Raises:
            Exception: Se ocorrer um erro ao finalizar os pedidos.
        """
        try:
            self._click(PageMainLocators.CHECKBOX_AGREE_TERMS)
            self._click(PageMainLocators.BUTTON_SUBMIT_ORDER)
        except Exception as error:
            raise Exception(f'Erro ao finalizar os pedidos: {error}')


    def get_time(self) -> Tuple[str, str]:
        """
        Captura o tempo e a acurácia do processamento da ordem.

        Este método utiliza os localizadores definidos na classe
        PageMainLocators para obter o texto exibido na tela referente
        ao tempo e à acurácia.

        Returns:
            Tuple[str, str]: O tempo e a acurácia capturados.

        Raises:
            Exception: Se ocorrer um erro ao capturar o tempo e a acurácia.
        """
        try:
            text_time = self._get_text(PageMainLocators.TIME_SCORING)
            text_accuracy = self._get_text(PageMainLocators.ACCURACY)
            return text_time, text_accuracy
        except Exception as error:
            raise Exception(
                f'Erro ao capturar o tempo e acurácia ao final do processo: {error}'
            )