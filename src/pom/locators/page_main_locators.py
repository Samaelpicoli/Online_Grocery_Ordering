from selenium.webdriver.common.by import By

from src.pom.locators.locator import Locator



class PageMainLocators:
    """
    Localizadores para elementos na página principal do site.
    
     O POM organiza o código de automação em classes que representam
    páginas específicas da aplicação web. Cada classe contém métodos
    que correspondem às ações que podem ser realizadas nessa página.

    Esse padrão torna o código mais modular e reutilizável,
    facilitando a manutenção e a leitura.

    Isso facilita a modificação de locadores, pois, se um seletor mudar,
    apenas a definição no localizador precisa ser atualizada,
    sem a necessidade de alterar várias partes do código.
    """

    BUTTON_DOWNLOAD = Locator(By.CSS_SELECTOR, "a.btn.btn-success")
    INPUT_ORDER_FOOD = Locator(By.ID, 'myInput')
    BUTTON_ADD_ITEM = Locator(By.ID, 'add_button')
    CHECKBOX_AGREE_TERMS = Locator(By.ID, 'agreeToTermsYes')
    BUTTON_SUBMIT_ORDER = Locator(By.ID, 'submit_button')
    TIME_SCORING = Locator(By.ID, 'processing-time')
    ACCURACY = Locator(By.ID, 'accuracy')
