from selenium.webdriver.common.by import By

from src.pom.locators.locator import Locator



class PageLoginLocators:
    """
    Localizadores para elementos na página de login do site.

    O POM organiza o código de automação em classes que representam
    páginas específicas da aplicação web. Cada classe contém métodos
    que correspondem às ações que podem ser realizadas nessa página.

    Esse padrão torna o código mais modular e reutilizável,
    facilitando a manutenção e a leitura.

    Isso facilita a modificação de locadores, pois, se um seletor mudar,
    apenas a definição no localizador precisa ser atualizada,
    sem a necessidade de alterar várias partes do código.
    """

    BUTTON_LOGIN_COMMUNITY = Locator(
        By.CSS_SELECTOR, 'button[aria-label="Community login"]'
    )

    INPUT_EMAIL = Locator(By.CLASS_NAME, 'textbox')
    BUTTON_NEXT = Locator(By.CLASS_NAME, 'slds-button')
    INPUT_PASSWORD = Locator(
        By.CSS_SELECTOR, 'input.textbox.input.sfdc_passwordinput.sfdc.input'
    )

    BUTTON_LOG_IN = Locator(By.CLASS_NAME, 'slds-button_brand')
    COOKIE_BUTTON = Locator(By.ID, 'onetrust-accept-btn-handler')




