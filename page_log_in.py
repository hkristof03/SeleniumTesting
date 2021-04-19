from selenium import webdriver
from selenium.webdriver.common.by import By

from page_main import PageMain


class PageLogIn(PageMain):

    def __init__(self, driver: webdriver, page_main_url: str,
                 page_log_in_url: str, **kwargs) -> None:
        super().__init__(driver, page_main_url)
        self.page_log_in_url = page_log_in_url

    def log_in(self, username: str, password: str, xpath_text: str,
               **kwargs) -> str:
        """"""
        url = self.page_log_in_url.replace("{username}", username)
        url = url.replace("{password}", password)
        self.driver.get(url)
        return self.wait_until_visible_and_return_element(
            (By.XPATH, xpath_text)).text
