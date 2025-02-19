from src.pom.web_driver_base_actions import WebDriverBaseActions
from src.pom.locators.page_login_locators import PageLoginLocators


class PageLogin(WebDriverBaseActions):
    """
    Classe para interações na página de login da aplicação web.

    Esta classe utiliza o padrão de design Page Object Model (POM) para
    encapsular a lógica de interação com os elementos da página de login.
    O POM ajuda a manter o código organizado, permitindo a separação
    entre a lógica de teste e a estrutura da página.

    Attributes:
        driver (WebDriver): A instância do Selenium WebDriver,
        herdada da classe base.
    """

    def __init__(self):
        """
        Inicializa a página de login chamando o construtor da classe base.

        A classe base WebDriverBaseActions fornece métodos comuns para
        interações com o WebDriver, como clicar em elementos e digitar texto.
        """
        super().__init__()

    
    def perform_login(self, email: str, password: str):
        """
        Realiza o login na aplicação utilizando as credenciais fornecidas.

        Este método interage com os elementos da página de login usando os
        localizadores definidos na classe PageLoginLocators. O uso do POM
        permite que as interações com a página sejam facilmente gerenciadas
        e mantidas.

        Args:
            email (str): O endereço de email do usuário.
            password (str): A senha do usuário.

        Raises:
            Exception: Se ocorrer um erro durante o processo de login.
        """
        try:
            self._click(PageLoginLocators.COOKIE_BUTTON)
            self.driver.implicitly_wait(5)
            self._click(PageLoginLocators.BUTTON_LOGIN_COMMUNITY)
            self._type_input(PageLoginLocators.INPUT_EMAIL, email)
            self._click(PageLoginLocators.BUTTON_NEXT)
            self._type_input(PageLoginLocators.INPUT_PASSWORD, password)
            self._click(PageLoginLocators.BUTTON_LOG_IN)
        except Exception as error:
            raise Exception(
                f'Erro ao realizar o login no site Grocery Ordering: {error}'
            )