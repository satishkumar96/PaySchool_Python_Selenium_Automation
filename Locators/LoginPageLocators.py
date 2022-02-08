from Locators.ReadExcelCellValue import read_data_from_excel


class get__login_locator_value:
    BAR_MENU_ICON = read_data_from_excel("LoginPage", 2, 2)
    BAR_MENU_TABS = read_data_from_excel("LoginPage", 3, 2)
    BACK_TO_SIGN_IN = read_data_from_excel("LoginPage", 4, 2)
    USERNAME = read_data_from_excel("LoginPage", 5, 2)
    PASSWORD = read_data_from_excel("LoginPage", 6, 2)
    SUBMIT_BUTTON = read_data_from_excel("LoginPage", 7, 2)
    INVALID_ERROR_MESSAGE = read_data_from_excel("LoginPage", 8, 2)
    PASSWORD_RESET = read_data_from_excel("LoginPage", 9, 2)
    PRIVACY_POLICY = read_data_from_excel("LoginPage", 10, 2)
    TERMS_AND_CONDITION = read_data_from_excel("LoginPage", 11, 2)