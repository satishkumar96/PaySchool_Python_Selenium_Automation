from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Locators.LoginPageLocators import get__login_locator_value


class LoginPage(BasePage):
    USERNAME = (By.XPATH, get__login_locator_value.USERNAME)
    PASSWORD = (By.XPATH, get__login_locator_value.PASSWORD)
    LOGIN_BUTTON = (By.XPATH, get__login_locator_value.SUBMIT_BUTTON)
    ERROR_MESSAGE = (By.XPATH, get__login_locator_value.INVALID_ERROR_MESSAGE)

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