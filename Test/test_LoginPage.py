from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Test.BasicTest import BaseTest
from Configuration.ConfigTest import init_driver


class Test_LoginPage(BaseTest):
    def test_title_page(self):
        self.lp = LoginPage(self.driver)
        self.lp.get_title()

    def test_password_reset(self):
        self.lp = LoginPage(self.driver)
        self.lp.password_reset()

    def test_privacy_policy(self):
        self.lp = LoginPage(self.driver)
        self.lp.privacy_policy()

    def test_bar_menu_icon(self):
        self.lp = LoginPage(self.driver)
        self.lp.bar_menu_icon()

    def test_positive_login(self):
        self.lp = LoginPage(self.driver)
        self.lp.do_positive_login()
        self.hp = HomePage(self.driver)
        self.hp.do_logout()

    def test_bar_menu_tabs(self):
        self.lp = LoginPage(self.driver)
        self.lp.bar_menu_tabs()

    def test_negative_login(self):
        self.lp = LoginPage(self.driver)
        self.lp.do_negative_login()