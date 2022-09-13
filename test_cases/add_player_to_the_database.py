import os
import time
import unittest

import self as self
from selenium import webdriver

from pages.add_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()
        add_player = AddPlayer(self.driver)
        add_player.type_in_player_name('Leon')
        add_player.type_in_player_surname('King')
        add_player.type_in_player_age('01012002')
        add_player.type_in_player_main_position('goalkeeper')
        add_player.click_on_the_submit_button()
        time.sleep(5)
        add_player.verify_new_player()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
