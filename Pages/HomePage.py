import time
import rpa
from Locators.HomePageLocators import get__home_page_locator_value
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    RIGHT_ARROW = (By.XPATH, get__home_page_locator_value.RIGHT_ARROW_BUTTON)
    LOGOUT = (By.XPATH, get__home_page_locator_value.LOGOUT_TAB)
    PATRON_TAB = (By.XPATH, get__home_page_locator_value.PATRON_TAB)
    HOME_TAB = (By.XPATH, get__home_page_locator_value.HOME_TAB)
    SEARCH_PATRON = (By.XPATH, get__home_page_locator_value.SEARCH_PATRON)
    SEARCH_BUTTON = (By.XPATH, get__home_page_locator_value.SEARCH_BUTTON)
    SEARCH_INPUT_BOX = (By.XPATH, get__home_page_locator_value.SEARCH_INPUT_BOX)
    REPORT_TAB = (By.XPATH, get__home_page_locator_value.REPORTS)
    NURSE_TRACKING = (By.XPATH, get__home_page_locator_value.NURSE_TRACKING)
    QUICK_APPS = (By.XPATH, get__home_page_locator_value.QUICK_APPS)
    FORMS = (By.XPATH, get__home_page_locator_value.FORMS)
    SCHOOL_PROGRAMS = (By.XPATH, get__home_page_locator_value.SCHOOL_PROGRAMS)
    FIRST_PATRON = (By.XPATH, get__home_page_locator_value.FIRST_PATRON)
    QUICK_LUNCH_RESTRICTION = (By.XPATH, get__home_page_locator_value.QUICK_LUNCH_RESTRICTION)
    DAILY_SPEND_LIMIT = (By.XPATH, get__home_page_locator_value.DAILY_SPEND_LIMIT)
    NO_A_LA_CARTE = (By.XPATH, get__home_page_locator_value.NO_A_LA_CARTE)
    NO_BREAKFAST = (By.XPATH, get__home_page_locator_value.NO_BREAKFAST)
    NO_SECOND_MEAL = (By.XPATH, get__home_page_locator_value.NO_SECOND_MEAL)
    ITEM_GROUPS_NOT_ALLOWED_LIST = (By.XPATH, get__home_page_locator_value.ITEM_GROUPS_NOT_ALLOWED_LIST)
    ITEMS_NOT_ALLOWED_LIST = (By.XPATH, get__home_page_locator_value.ITEMS_NOT_ALLOWED_LIST)
    ITEM_GROUP_NOT_ALLOWED = (By.XPATH, get__home_page_locator_value.ITEM_GROUP_NOT_ALLOWED)
    ITEMS_NOT_ALLOWED = (By.XPATH, get__home_page_locator_value.ITEMS_NOT_ALLOWED)

    def __init__(self, driver):
        super().__init__(driver)

    def do_logout(self):
        self.move_to_element(self.RIGHT_ARROW).perform()
        self.click(self.LOGOUT)
        self.get_alert().accept()

    def verify_home_tab(self):
        assert self.display_element(self.HOME_TAB)

    def verify_patron_tab(self):
        assert self.display_element(self.PATRON_TAB)

    def verify_report_tab(self):
        assert self.display_element(self.REPORT_TAB)

    def verify_nurse_tracking(self):
        assert self.display_element(self.NURSE_TRACKING)

    def verify_quick_apps(self):
        assert self.display_element(self.QUICK_APPS)

    def verify_forms(self):
        assert self.display_element(self.FORMS)

    def mouse_over_patron_tab(self):
        self.verify_patron_tab()
        self.move_to_element(self.PATRON_TAB).perform()

    def select_search_patron(self):
        self.mouse_over_patron_tab()
        assert self.display_element(self.SEARCH_PATRON)
        self.click(self.SEARCH_PATRON)

    def verify_search_box(self):
        assert self.display_element(self.SEARCH_INPUT_BOX)

    def verify_search_button(self):
        assert self.display_element(self.SEARCH_BUTTON)

    def search_a_patron(self):
        self.verify_search_box()
        self.send_keys(self.SEARCH_INPUT_BOX, "michael")

    def click_search_button(self):
        self.verify_search_button()
        self.click(self.SEARCH_BUTTON)

    def verify_first_patron(self):
        assert self.display_element(self.FIRST_PATRON)

    def click_first_patron(self):
        self.verify_first_patron()
        self.click(self.FIRST_PATRON)

    def verify_quick_lunch_restriction(self):
        assert self.display_element(self.QUICK_LUNCH_RESTRICTION)

    def click_quick_lunch_restriction(self):
        self.verify_quick_lunch_restriction()
        self.click(self.QUICK_LUNCH_RESTRICTION)

    def verify_daily_spend_limit(self):
        assert self.display_element(self.DAILY_SPEND_LIMIT)

    def daily_spend_limit(self):
        self.verify_daily_spend_limit()
        self.send_keys(self.DAILY_SPEND_LIMIT, "123")

    def verify_no_a_la_carte(self):
        assert self.display_element(self.NO_A_LA_CARTE)

    def verify_no_breakfast(self):
        assert self.display_element(self.NO_BREAKFAST)

    def verify_no_second_meal(self):
        assert self.display_element(self.NO_SECOND_MEAL)

    def click_no_a_la_carte(self):
        self.verify_no_a_la_carte()
        self.click_elements(self.NO_A_LA_CARTE)

    def click_no_second_meal(self):
        self.verify_no_second_meal()
        self.click_elements(self.NO_SECOND_MEAL)

    def click_no_breakfast(self):
        self.verify_no_breakfast()
        self.click_elements(self.NO_BREAKFAST)

    def verify_item_groups_not_allowed(self):
        assert self.display_element(self.ITEM_GROUP_NOT_ALLOWED)

    def item_groups_not_allowed(self):
        self.verify_item_groups_not_allowed()
        self.click(self.ITEM_GROUP_NOT_ALLOWED)

    def item_groups_not_allowed_dropdown(self):
        self.click_elements(self.ITEM_GROUPS_NOT_ALLOWED_LIST)
        self.click(self.ITEM_GROUP_NOT_ALLOWED)
        time.sleep(2)

    def verify_item_not_allowed(self):
        assert self.display_element(self.ITEMS_NOT_ALLOWED)

    def item_not_allowed(self):
        self.verify_item_not_allowed()
        self.click(self.ITEMS_NOT_ALLOWED)

    def item_not_allowed_dropdown(self):
        self.click_elements(self.ITEMS_NOT_ALLOWED_LIST)
        self.click(self.ITEMS_NOT_ALLOWED)

    def click_report_tab(self):
        self.verify_report_tab()
        rpa.init(visual_automation=True)
        rpa.click(self.REPORT_TAB)
        rpa.close()
