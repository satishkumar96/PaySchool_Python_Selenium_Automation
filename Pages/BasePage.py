from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        print(self.driver.title)

    def element_wait(self, by_loc):
        return WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(by_loc))

    def element_click_wait(self, by_loc):
        return WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(by_loc))

    def elements_wait(self, by_loc):
        return WebDriverWait(self.driver, 50).until(EC.visibility_of_all_elements_located(by_loc))

    def send_keys(self, by_loc, text):
        self.element_wait(by_loc).send_keys(text)

    def click(self, by_loc):
        self.element_click_wait(by_loc).click()

    def get_text(self, by_loc):
        return self.element_wait(by_loc).text

    def move_to_element(self, by_loc):
        return ActionChains(self.driver).move_to_element(self.element_wait(by_loc))

    def display_element(self, by_loc):
        return self.element_wait(by_loc).is_displayed()

    def get_alert(self):
        return Alert(self.driver)

    def click_elements(self, by_loc):
        elements = self.elements_wait(by_loc)

        for ele in elements:
            ele.click()
