from Locators.HomePageLocators import get__home_page_locator_value
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    RIGHT_ARROW = (By.XPATH, get__home_page_locator_value.RIGHT_ARROW_BUTTON)
    LOGOUT = (By.XPATH, get__home_page_locator_value.LOGOUT_TAB)

    def __init__(self, driver):
        super().__init__(driver)

    def do_logout(self):
        self.move_to_element(self.RIGHT_ARROW).perform()
        self.click(self.LOGOUT)
        self.get_alert().accept()