from selenium import webdriver
from selenium.webdriver.common.by import By

from page_main import PageMain


class PageFileUpload(PageMain):

    def __init__(self, driver: webdriver, page_main_url: str,
                 xpath_page: str, **kwargs) -> None:

        super().__init__(driver, page_main_url)
        self.xpath_page = xpath_page
        self.go_to_page(xpath_page)

    def upload_file(
        self,
        xpath_choose_file: str,
        path_file: str,
        xpath_upload: str,
        xpath_result: str,
        **kwargs,
    ) -> str:
        """"""
        wec = self.wait_until_visible_and_return_element(
            (By.XPATH, xpath_choose_file)
        )
        wec.send_keys(path_file)
        weu = self.wait_until_visible_and_return_element(
            (By.XPATH, xpath_upload)
        )
        weu.click()
        return self.wait_until_visible_and_return_element(
            (By.XPATH, xpath_result)
        ).text
