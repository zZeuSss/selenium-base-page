from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

web_drivers = {
    'Firefox': webdriver.Firefox(), 'Chrome': webdriver.Chrome(),
    'Edge': webdriver.Edge(), 'Ie': webdriver.Ie(),
    'Opera': webdriver.Opera(), 'Safari': webdriver.Safari()
}


class BasePage:

    driver = None
    url = None

    def __init__(self, url="127.0.0.1", browser_name="Firefox"):
        self.base_url = url
        try:
            self.driver = web_drivers.get(browser_name)
        except:
            print(f"Can't create connection with {browser_name}")

    @property
    def __wait(self, timeout: int = 10) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    def find_element(self, locator, time: int = 10):
        return self.__wait(time).until(EC.presence_of_element_located(locator),
                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time: int = 10):
        return self.__wait(time).until(EC.presence_of_all_elements_located(locator),
                                       message=f"Can't find elements by locator {locator}")

    def go_to_site(self, url: str = "127.0.0.1"):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()

    def get_title(self):
        return self.driver.title
