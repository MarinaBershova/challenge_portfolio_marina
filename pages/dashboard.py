from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "(//span[contains(@class, "MuiTypography-root")])[1]"
    players_xpath = "(//span[contains(@class, "MuiTypography-root")])[2]"
    language_xpath = "(//span[contains(@class, "MuiTypography-root")])[3]"
    sign_out_xpath = "(//span[contains(@class, "MuiTypography-root")])[4]"
    pass