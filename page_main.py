from selenium import webdriver
from selenium.webdriver.common.by import By

from page_base import PageBase


class PageMain(PageBase):

    def __init__(self, driver: webdriver, page_main_url: str,
                 **kwargs) -> None:

        super().__init__(driver)
        self.page_main_url = page_main_url
        self.driver.get(page_main_url)

    def go_to_page(self, xpath: str, **kwargs) -> None:
        self.driver.find_element(By.XPATH, xpath).click()
        self.wait_implicitly(2)
        
    def go_back(self) -> None:
        self.driver.back()
        self.wait_implicitly(2)

    def get_page_title(self) -> str:
        return self.driver.title




