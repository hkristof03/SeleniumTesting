from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from page_main import PageMain


class PageHover(PageMain):

    def __init__(self, driver: webdriver, page_main_url: str,
                 page_hover_url: str, **kwargs) -> None:
        super().__init__(driver, page_main_url)
        self.page_hover_url = page_hover_url
        self.driver.get(self.page_hover_url)

    def hover_perform(self, xpath_first_level: str, xpath_second_level: str,
                      xpath_text: str, **kwargs) -> str:
        """"""
        element = self.wait_until_visible_and_return_multiple_elements(
            (By.XPATH, xpath_first_level)
        )[0]
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        second_element = element.find_element_by_xpath(xpath_second_level)
        action.move_to_element(second_element).perform()
        second_element.click()
        text = self.wait_until_visible_and_return_element(
            (By.XPATH, xpath_text)).text
        return text
