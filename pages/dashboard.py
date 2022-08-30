import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    header_xpath = "//h6[text()='Scouts Panel']"
    main_page_xpath = "(//span[contains(@class, 'MuiTypography-root')])[1]"
    players_xpath = "(//span[contains(@class, 'MuiTypography-root')])[2]"
    language_button_xpath = "(//span[contains(@class, 'MuiTypography-root')])[3]"
    language_button = "English"
    sign_out_button_xpath = "(//span[contains(@class, 'MuiTypography-root')])[4]"
    players_count_xpath = "//*[text()='Players count']"
    matches_count_xpath = "//*[text()='Matches count']"
    reports_count_xpath = "//*[text()='Reports count']"
    events_count_xpath = "//*[text()='Events count']"
    logo_xpath = "//*[@title='Logo Scouts Panel']"
    scouts_panel_xpath = "//h2[text()='Scouts Panel']"
    management_panel_xpath = "//p[contains(@class, 'MuiTypography-root')]"
    dev_team_contact_xpath = "//*[text()='Dev team contact']"
    shortcuts_xpath = "//h2[text()='Shortcuts']"
    add_player_button_xpath = "//*[text()='Add player']"
    activity_xpath = "//h2[text()='Activity']"
    edit_last_created_player_xpath = "//*[text()='test_name test_surname']"
    edit_last_updated_player_xpath = "//*[text()='Tester Tester']"
    last_updated_report_xpath = "//*[text()='Test Testowy']"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.dev_team_contact_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_language_button(self):
        self.click_on_the_element(self.language_button_xpath)

    def verify_language_button(self):
        self.assert_element_text(self.language_button_xpath, self.language_button)

    def click_on_the_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)