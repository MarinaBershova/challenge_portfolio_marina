import time

from pages.base_page import BasePage

class AddPlayer(BasePage):
    player_name_xpath = "// *[ @ name='name']"
    player_surname_xpath = "//*[@name='surname']"
    player_age_xpath = "//*[@name='age']"
    player_main_position_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[text()='Submit']"
    clear_button_xpath = "//*[text()='Clear']"

    def type_in_player_name(self, name):
        self.field_send_keys(self.player_name_xpath, name)

    def type_in_player_surname(self, surname):
        self.field_send_keys(self.player_surname_xpath, surname)

