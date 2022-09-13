import os
import time
import unittest

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestInvalidLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_invalid_login_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.click_on_the_sign_in_button()
        user_login.verify_warning_massage()
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()