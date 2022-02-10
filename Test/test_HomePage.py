from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Test.BasicTest import BaseTest
from Test.test_LoginPage import init_driver


class Test_HomePage(BaseTest):
    def test_verify_home_tab(self):
        self.lp = LoginPage(self.driver)
        self.lp.do_positive_login()
        self.hp = HomePage(self.driver)
        self.hp.verify_home_tab()

    def test_verify_patron_tab(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_patron_tab()

    def test_verify_reports(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_report_tab()

    def test_verify_nurse_tracking(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_nurse_tracking()

    def test_verify_quick_apps(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_quick_apps()

    def test_mouse_over_patron_tab(self):
        self.hp = HomePage(self.driver)
        self.hp.mouse_over_patron_tab()

    def test_select_patron_tab(self):
        self.hp = HomePage(self.driver)
        self.hp.select_search_patron()

    def test_verify_search_box(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_search_box()

    def test_search_a_patron(self):
        self.hp = HomePage(self.driver)
        self.hp.search_a_patron()

    def test_verify_search_button(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_search_button()

    def test_click_search_button(self):
        self.hp = HomePage(self.driver)
        self.hp.click_search_button()

    def test_verify_first_patron(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_first_patron()

    def test_click_first_patron(self):
        self.hp = HomePage(self.driver)
        self.hp.click_first_patron()

    def test_verify_quick_lunch_restriction(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_quick_lunch_restriction()

    def test_click_quick_lunch_restriction(self):
        self.hp = HomePage(self.driver)
        self.hp.click_quick_lunch_restriction()

    def test_verify_daily_spend_limit(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_daily_spend_limit()

    def test_daily_spend_limit(self):
        self.hp = HomePage(self.driver)
        self.hp.daily_spend_limit()

    def test_verify_no_a_la_carte(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_no_a_la_carte()

    def test_verify_no_breakfast(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_no_breakfast()

    def test_verify_no_second_meal(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_no_second_meal()

    def test_click_no_a_la_carte(self):
        self.hp = HomePage(self.driver)
        self.hp.click_no_a_la_carte()

    def test_click_no_breakfast(self):
        self.hp = HomePage(self.driver)
        self.hp.click_no_breakfast()

    def test_click_no_second_meal(self):
        self.hp = HomePage(self.driver)
        self.hp.click_no_second_meal()

    def test_verify_item_groups_not_allowed(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_item_groups_not_allowed()

    def test_click_item_groups_not_allowed(self):
        self.hp = HomePage(self.driver)
        self.hp.item_groups_not_allowed()

    def test_click_item_groups_not_allowed_dropdown(self):
        self.hp = HomePage(self.driver)
        self.hp.item_groups_not_allowed_dropdown()

    def test_verify_item_not_allowed(self):
        self.hp = HomePage(self.driver)
        self.hp.verify_item_not_allowed()

    def test_item_not_allowed(self):
        self.hp = HomePage(self.driver)
        self.hp.item_not_allowed()

    def test_item_not_allowed_dropdown(self):
        self.hp = HomePage(self.driver)
        self.hp.item_not_allowed_dropdown()
