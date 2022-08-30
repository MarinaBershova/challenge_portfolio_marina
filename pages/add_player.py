import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    player_name_xpath = "// *[ @ name='name']"
    player_surname_xpath = "//*[@name='surname']"
    player_age_xpath = "//*[@name='age']"
    player_main_position_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[text()='Submit']"
    clear_button_xpath = "//*[text()='Clear']"
    new_player_xpath = "(//span[contains(@class, 'MuiTypography-root')])[3]"
    new_player = "Leon King"

    def type_in_player_name(self, name):
        self.field_send_keys(self.player_name_xpath, name)

    def type_in_player_surname(self, surname):
        self.field_send_keys(self.player_surname_xpath, surname)

    def type_in_player_age(self, age):
        self.field_send_keys(self.player_age_xpath, age)

    def type_in_player_main_position(self, main_position):
        self.field_send_keys(self.player_main_position_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def verify_new_player(self):
        self.assert_element_text(self.new_player_xpath, self.new_player)

    def click_on_the_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)