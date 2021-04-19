from selenium import webdriver

from page_main import PageMain


class PageDropDown(PageMain):

    def __init__(self, driver: webdriver, page_main_url: str,
                 page_dropdown_url: str, **kwargs) -> None:
        super().__init__(driver, page_main_url)
        self.page_dropdown_url = page_dropdown_url
        self.driver.get(self.page_dropdown_url)

    def read_select_dropdown(self, locator: tuple, **kwargs) -> list:
        """"""
        options = self.wait_until_visible_and_return_multiple_elements(locator)
        texts_options = []
        for opt in options:
            texts_options.append(opt.text)
            opt.click()
        return texts_options
