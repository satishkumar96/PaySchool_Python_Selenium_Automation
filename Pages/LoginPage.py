import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Locators.LoginPageLocators import get__login_locator_value


class LoginPage(BasePage):
    USERNAME = (By.XPATH, get__login_locator_value.USERNAME)
    PASSWORD = (By.XPATH, get__login_locator_value.PASSWORD)
    LOGIN_BUTTON = (By.XPATH, get__login_locator_value.SUBMIT_BUTTON)
    ERROR_MESSAGE = (By.XPATH, get__login_locator_value.INVALID_ERROR_MESSAGE)
    PASSWORD_RESET_BUTTON = (By.XPATH, get__login_locator_value.PASSWORD_RESET)
    BACK_TO_SIGN_IN_BUTTON = (By.XPATH, get__login_locator_value.BACK_TO_SIGN_IN)
    PRIVACY_POLICY = (By.XPATH, get__login_locator_value.PRIVACY_POLICY)
    BAR_MENU_ICON = (By.XPATH, get__login_locator_value.BAR_MENU_ICON)
    BAR_MENU_TABS = (By.XPATH, get__login_locator_value.BAR_MENU_TABS)

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

    def password_reset(self):
        self.click(self.PASSWORD_RESET_BUTTON)
        self.click(self.BACK_TO_SIGN_IN_BUTTON)

    def privacy_policy(self):
        assert self.display_element(self.PRIVACY_POLICY)

    def bar_menu_icon(self):
        assert self.display_element(self.BAR_MENU_ICON)

    def bar_menu_tabs(self):
        self.click(self.BAR_MENU_ICON)
        self.click_elements(self.BAR_MENU_TABS)
        self.click(self.BACK_TO_SIGN_IN_BUTTON)
