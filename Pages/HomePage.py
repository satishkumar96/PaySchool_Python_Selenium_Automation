import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    RIGHT_ARROW = (By.XPATH, '//a[@class="rmRightArrow"]')
    LOGOUT = (By.XPATH, "//span[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def do_logout(self):
        self.move_to_element(self.RIGHT_ARROW).perform()
        self.click(self.LOGOUT)
        self.get_alert().accept()