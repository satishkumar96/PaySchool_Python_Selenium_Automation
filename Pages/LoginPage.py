from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME = (By.ID, "TextUsername")
    PASSWORD = (By.ID, "TextPassword")
    LOGIN_BUTTON = (By.NAME, "ctl56")
    ERROR_MESSAGE = (By.XPATH, '//span[@id="LabelError"]')

    def __init__(self, driver):
        super().__init__(driver)

    def do_positive_login(self):
        self.send_keys(self.USERNAME, "chimerasa")
        self.send_keys(self.PASSWORD, "Test2021")
        self.click(self.LOGIN_BUTTON)

    def do_negative_login(self):
        self.send_keys(self.USERNAME, "chimeras")
        self.send_keys(self.PASSWORD, "Test202")
        self.click(self.LOGIN_BUTTON)
        print(self.get_text(self.ERROR_MESSAGE))
