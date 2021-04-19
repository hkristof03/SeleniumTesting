from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By

from page_main import PageMain
from drag_andr_drop_javascript import drag_and_drop


class DragAndDrop(PageMain):

    def __init__(self, driver: webdriver, page_main_url: str,
                 page_drag_and_drop_url: str, **kwargs) -> None:
        super().__init__(driver, page_main_url)
        self.page_drag_and_drop_url = page_drag_and_drop_url
        self.driver.get(self.page_drag_and_drop_url)

    def perform_drag_and_drop(self, xpath_source: str,
                              xpath_target: str, **kwargs) -> List[tuple]:
        """"""

        source = self.wait_until_visible_and_return_element(
            (By.XPATH, xpath_source))
        target = self.wait_until_visible_and_return_element(
            (By.XPATH, xpath_target))

        source_txt = source.text
        target_txt = target.text
        drag_and_drop(self.driver, source, target)

        return [(source_txt, target_txt), (source.text, target.text)]

