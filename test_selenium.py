import os
from copy import deepcopy
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from page_main import PageMain
from page_sign_in import PageSignIn
from page_log_in import PageLogIn
from page_file_upload import PageFileUpload
from page_dropdown import PageDropDown
from page_secure_download import PageSecureDownload
from cookie import CookieManipulator
from drag_and_drop import DragAndDrop
from page_hover import PageHover
from utilities import load_yaml


class TestTheInternetHerokuApp(unittest.TestCase):

    path_dir = os.path.dirname(__file__)
    path_data_test = os.path.join(path_dir, 'data_test')
    config = load_yaml(os.path.join(path_dir, 'configs', 'test_config.yaml'))

    def setUp(self):

        path_chrome_driver = os.path.join(self.path_dir, 'chrome_driver',
                                          'chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(path_chrome_driver,
                                       options=chrome_options)

    def test_extendable_static_pages(self):
        # Setup
        config_pm = self.config['page_main']
        config_tesp = config_pm['test_extendable_static_pages']
        xpath = config_tesp['xpath']
        xpath_result = config_tesp['xpath_result']
        test_data = config_tesp['test_data']
        pm = PageMain(self.driver, **config_pm)
        # Exercise
        for td in test_data:
            href, desired_text = td
            xp = deepcopy(xpath).replace("{}", href)
            pm.go_to_page(xp)
            actual_text = pm.wait_until_visible_and_return_element(
                (By.XPATH, xpath_result)
            ).text
            # Verify
            assert desired_text == actual_text
            pm.go_back()

    def test_go_to_sign_in_page(self):
        # Setup
        config_pm = self.config['page_main']
        config_go_to_sign_in = config_pm['go_to_sign_in']
        desired_text = config_go_to_sign_in['desired_text']
        pm = PageMain(self.driver, **config_pm)
        locator = config_go_to_sign_in['locator']
        # Exercise
        pm.go_to_page(**config_go_to_sign_in)
        actual_text = pm.wait_until_visible_and_return_element(
            (By.XPATH, locator)).text
        # Verify
        assert desired_text == actual_text

    def test_sign_in(self):
        # Setup
        config_psi = self.config['page_main']
        config_psi.update(**self.config['page_sign_in'])
        config_test_sign_in = config_psi['test_sign_in']
        desired_text = config_test_sign_in['desired_text']
        psi = PageSignIn(self.driver, **config_psi)
        # Exercise
        actual_text = psi.login_valid_user(**config_test_sign_in)
        # Verify
        assert desired_text in actual_text

    def test_log_in(self):
        # Setup
        config_pli = self.config['page_main']
        config_pli.update(**self.config['page_log_in'])
        config_test_log_in = config_pli['test_log_in']
        desired_text = config_test_log_in['desired_text']
        pli = PageLogIn(self.driver, **config_pli)
        # Exercise
        actual_text = pli.log_in(**config_test_log_in)
        # Verify
        assert desired_text == actual_text

    def test_upload_file(self):
        # Setup
        config_pfu = self.config['page_main']
        config_pfu.update(**self.config['page_file_upload'])
        config_test_upload_file = config_pfu['test_upload_file']
        path_file = os.path.join(self.path_data_test,
                                 config_test_upload_file.get('file_name'))
        config_test_upload_file.update({'path_file': path_file})
        pfu = PageFileUpload(self.driver, **config_pfu)
        desired_text = config_test_upload_file['desired_text']
        # Exercise
        actual_text = pfu.upload_file(**config_test_upload_file)
        # Verify
        assert desired_text == actual_text

    def test_read_select_dropdown(self):
        # Setup
        config_pdd = self.config['page_main']
        config_pdd.update(**self.config['page_dropdown'])
        config_read_select_dropdown = config_pdd['test_read_select_dropdown']
        desired_options = config_read_select_dropdown['desired_options']
        pdd = PageDropDown(self.driver, **config_pdd)
        # Exercise
        actual_options = pdd.read_select_dropdown(
            (By.XPATH, config_read_select_dropdown['xpath'])
        )
        # Verify
        assert desired_options == actual_options

    def test_secure_download(self):
        # Setup
        config_psd = self.config['page_main']
        config_psd.update(**self.config['page_secure_download'])
        config_test_page_secure_download = config_psd['test_secure_download']
        path_download = os.path.join(self.path_dir,
                                     config_psd['path_download'])
        config_psd.update({'path_download': path_download})
        psd = PageSecureDownload(self.driver, **config_psd)
        # Exercise
        path_files = psd.secure_download(
            (By.XPATH, config_test_page_secure_download['xpath'])
        )
        # Verify
        for pf in path_files:
            assert os.path.isfile(pf)
        psd.remove_downloaded_files(path_files)
        assert not os.listdir(psd.path_download)
    
    def test_cookie_manipulations(self):
        # Setup
        config_page_main = self.config['page_main']
        config_cookie = self.config['cookie_manipulator']
        desired_cookies = config_cookie['add_cookies']
        desired_cookie_names = [ck['name'] for ck in desired_cookies]
        desired_cookie = desired_cookies[0]
        pm = PageMain(self.driver, **config_page_main)
        cm = CookieManipulator(self.driver)
        # Exercise
        cm.add_cookies(desired_cookies)
        actual_cookie_names = [
            d['name'] for d in cm.get_all_cookies()
            if d['name'] in desired_cookie_names
        ]
        # Verify
        assert desired_cookie_names == actual_cookie_names
        # Exercise
        actual_cookie = cm.get_cookie_by_name(desired_cookie['name'])
        # Verify
        assert desired_cookie['name'] == actual_cookie['name']
        # Exercise
        cm.delete_cookie(desired_cookie['name'])
        # Verify
        assert not cm.get_cookie_by_name(desired_cookie['name'])
        # Exercise
        cm.delete_all_cookies()
        assert not cm.get_all_cookies()
    
    def test_drag_and_drop(self):
        # Setup
        config_page_dad = self.config['page_main']
        config_page_dad.update(**self.config['page_drag_and_drop'])
        config_test_drag_and_drop = config_page_dad['test_drag_and_drop']
        dad = DragAndDrop(self.driver, **config_page_dad)
        # Exercise
        result = dad.perform_drag_and_drop(**config_test_drag_and_drop)
        prev_src, prev_target = result[0]
        curr_src, curr_target = result[1]
        # Verify
        assert prev_src == curr_target and prev_target == curr_src
    
    def test_go_back_and_get_title(self):
        # Setup
        config_page_main = self.config['page_main']
        pm = PageMain(self.driver, **config_page_main)
        desired_title = config_page_main['go_back_and_get_title']['title']
        # Exercise
        pm.go_to_page(config_page_main['go_to_sign_in']['xpath'])
        pm.go_back()
        actual_title = pm.get_page_title()
        # Verify
        assert desired_title == actual_title

    def test_hover_perform(self):
        # Setup
        config_ph = self.config['page_main']
        config_ph.update(**self.config['page_hover'])
        config_test_hover_perform = config_ph['test_hover_perform']
        desired_text = config_test_hover_perform['desired_text']
        ph = PageHover(self.driver, **config_ph)
        # Exercise
        actual_text = ph.hover_perform(**config_test_hover_perform)
        # Verify
        assert desired_text == actual_text

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
