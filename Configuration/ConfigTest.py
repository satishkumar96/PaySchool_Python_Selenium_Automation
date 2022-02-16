import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    global driver
    if request.param == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    if request.param == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(100)
    driver.set_page_load_timeout(100)
    driver.get("https://alpha4a-test.sdms2.com/Default.aspx")
    driver.delete_all_cookies()
    yield
    driver.quit()
