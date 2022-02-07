from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Test.BasicTest import BaseTest
from Configuration.ConfigTest import init_driver

class Test_LoginPage(BaseTest):
    def test_title_page(self):
        self.lp = LoginPage(self.driver)
        self.lp.get_title()

    def test_positive_login(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.lp.do_positive_login()
        self.hp.do_logout()

    def test_negative_login(self):
        self.lp = LoginPage(self.driver)
        self.lp.do_negative_login()

