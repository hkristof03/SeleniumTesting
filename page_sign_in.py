from selenium import webdriver
from selenium.webdriver.common.by import By

from page_main import PageMain


class PageSignIn(PageMain):

    def __init__(self, driver: webdriver, page_main_url: str,
                 page_sign_in_url: str, xpath_username: str,
                 xpath_password: str, xpath_sign_in_button: str,
                 **kwargs) -> None:
        super().__init__(driver, page_main_url)
        self.page_sign_in_url = page_sign_in_url
        self.driver.get(self.page_sign_in_url)
        self.xpath_username = xpath_username
        self.xpath_password = xpath_password
        self.xpath_sign_in_button = xpath_sign_in_button

    def login_valid_user(self, username: str, password: str, xpath_text: str,
                         **kwargs) -> str:
        self.driver.find_element_by_xpath(self.xpath_username).send_keys(
            username)
        self.driver.find_element_by_xpath(self.xpath_password).send_keys(
            password)
        self.driver.find_element_by_xpath(self.xpath_sign_in_button).click()
        return self.wait_until_visible_and_return_element(
            (By.XPATH, xpath_text)
        ).text

