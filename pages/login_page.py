 from pages.base_page import BasePage


 class LoginPage(BasePage):
     header_xpath = "//div/h5"
     login_field_xpath = "//*[@id='login']"
     password_field_xpath = "//*[@name='password']"
     remind_password_hyperlink_xpath = "//*[text()='Remind password']"
     choosing_language_xpath = "//*[@value='en']"
     sign_in_button_xpath = "//*[@type='submit']"



     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)
