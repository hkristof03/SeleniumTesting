from typing import List

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class PageBase:

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_implicitly(self, seconds: int) -> None:
        # implicit wait
        self.driver.implicitly_wait(seconds)

    def wait_until_visible_and_return_element(
        self,
        locator: tuple,
        **kwargs
    ) -> WebElement:
        # explicit wait
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_visible_and_return_multiple_elements(
        self,
        locator: tuple
    ) -> List[WebElement]:
        # explicit wait
        return self.wait.until(EC.visibility_of_all_elements_located(locator))