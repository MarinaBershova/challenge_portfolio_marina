from pages.base_page import BasePage


class Dashboard(BasePage):
    header_xpath = "//h6[text()="Scouts Panel"]"
    main_page_xpath = "(//span[contains(@class, "MuiTypography-root")])[1]"
    players_xpath = "(//span[contains(@class, "MuiTypography-root")])[2]"
    language_xpath = "(//span[contains(@class, "MuiTypography-root")])[3]"
    sign_out_xpath = "(//span[contains(@class, "MuiTypography-root")])[4]"
    players_count_xpath = "//*[text()="Players count"]"
    matches_count_xpath = "//*[text()="Matches count"]"
    reports_count_xpath = "//*[text()="Reports count"]"
    events_count_xpath = "//*[text()="Events count"]"
    logo_xpath = "//*[@title="Logo Scouts Panel"]"
    scouts_panel_xpath = "//h2[text()="Scouts Panel"]"
    management_panel_xpath = "//p[contains(@class, "MuiTypography-root")]"
    dev_team_contact_xpath = "//*[text()="Dev team contact"]"
    shortcuts_xpath = "//h2[text()="Shortcuts"]"
    add_player_xpath = "//*[text()="Add player"]"

    pass