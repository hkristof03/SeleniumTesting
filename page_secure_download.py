import os
import requests
import shutil
from typing import List

from selenium import webdriver

from page_main import PageMain


class PageSecureDownload(PageMain):

    def __init__(self, driver: webdriver, page_main_url: str,
                 page_secure_download_url: str, username: str, password: str,
                 path_download: str, **kwargs) -> None:
        super().__init__(driver, page_main_url)
        page_log_in = page_secure_download_url.replace('{username}', username)
        page_log_in = page_log_in.replace('{password}', password)
        self.page_log_in = page_log_in
        self.page_secure_download_url = page_secure_download_url
        self.path_download = path_download
        self.driver.get(self.page_log_in)

    def secure_download(self, locator: tuple, **kwargs) -> List[str]:
        """"""
        path_files = []
        elements = self.wait_until_visible_and_return_multiple_elements(
            locator
        )
        for el in elements:
            url = el.get_attribute('href')
            fn = url.split('/')[-1]
            path_file_save = os.path.join(self.path_download, fn)
            self.download_file(url, path_file_save)
            path_files.append(path_file_save)
        return path_files

    @staticmethod
    def download_file(url: str, path_file_save: str) -> None:
        with requests.get(url, stream=True) as r:
            with open(path_file_save, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

    @staticmethod
    def remove_downloaded_files(path_files: List[str]) -> None:
        for pf in path_files:
            os.remove(pf)

