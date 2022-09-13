from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@name='password']"
    login_url = ('https://scouts.futbolkolektyw.pl/en/')
    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
    choosing_language_xpath = "//*[@value='en']"
    sign_in_button_xpath = "//*[@type='submit']"
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//div/h5"
    header_of_box = "Scouts Panel"
    warning_message_xpath = "//*[text()='Please provide your username or your e-mail.']"
    warning_message = "Please provide your username or your e-mail."

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def verify_title_of_box(self):
        self.assert_element_text(self.title_of_box_xpath, self.header_of_box)

    def verify_warning_massage(self):
        self.assert_element_text(self.warning_message_xpath, self.warning_message)
