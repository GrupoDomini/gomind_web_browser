from typing import Union
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class WebBrowser:
    def __init__(self) -> None:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium import webdriver

        self.nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def find_element(self, selector: str, by: str = By.XPATH):
        return self.nav.find_element(by, selector)

    def verify_if_element_exists(self, selector: str, by: str = By.XPATH) -> bool:
        """Retorna True se o elemento estiver em tela e False se não
        Coloquei dessa forma pois não sei se o 'v' será true,
        e se não existir o elemento nós receberemos um erro

        Args:
            selector (str): _description_
            by (str, optional): _description_. Defaults to By.XPATH.

        Returns:
            bool: _description_
        """
        try:
            v = bool(self.nav.find_element(by, selector))
            return v or True
        except Exception as _:
            return False

    def send_keys(self, selector: str, keys: str, by: str = By.XPATH):
        """Envia caracteres para um elemento que está em tela

        Args:
            selector (str): _description_
            keys (str): _description_
            by (str, optional): _description_. Defaults to By.XPATH.

        Returns:
            _type_: _description_
        """
        return self.nav.find_element(by, selector).send_keys(keys)

    def click(self, selector: str, by: str = By.XPATH):
        return self.nav.find_element(by, selector).click()

    def wait_for_element(
        self, selector: str, timeout: int = 10, by: str = By.XPATH
    ) -> bool:
        return bool(
            WebDriverWait(self.nav, timeout).until(
                expected_conditions.presence_of_element_located((by, selector))
            )
        )

    def click_with_action_chains(self, selector: str, by: str = By.XPATH):
        element = self.nav.find_element(by, selector)
        ActionChains(self.nav).move_to_element(
            element
        ).click_and_hold().release().perform()

    def encerrar_navegador(self) -> None:
        try:
            self.nav.close()
            self.nav.quit()
        except Exception as _:
            pass

    def get_cookie(self, cookie_name: str) -> Union[str, None]:
        """
        Retorna o valor de um cookie específico, se existir.
        """
        cookies = self.nav.get_cookies()
        for cookie in cookies:
            if cookie["name"] == cookie_name:
                return cookie["value"]
        return None

    def close(self) -> None:
        self.nav.close()

    def quit(self) -> None:
        self.nav.quit()
