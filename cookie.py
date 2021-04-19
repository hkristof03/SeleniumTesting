from typing import List

from selenium import webdriver


class CookieManipulator:

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def add_cookies(self, cookies: List[dict]) -> None:
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def get_cookie_by_name(self, name: str) -> dict:
        return self.driver.get_cookie(name)

    def get_all_cookies(self) -> dict:
        return self.driver.get_cookies()

    def delete_cookie(self, name: str) -> None:
        self.driver.delete_cookie(name)

    def delete_all_cookies(self) -> None:
        self.driver.delete_all_cookies()
