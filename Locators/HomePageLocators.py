from Locators.ReadExcelCellValue import read_data_from_excel


class get__home_page_locator_value:
    HOME_TAB = read_data_from_excel("HomePage", 2, 2)
    RIGHT_ARROW_BUTTON = read_data_from_excel("HomePage", 3, 2)
    LOGOUT_TAB = read_data_from_excel("HomePage", 4, 2)
    PATRON_TAB = read_data_from_excel("HomePage", 5, 2)
    SEARCH_PATRON = read_data_from_excel("HomePage", 6, 2)
    SEARCH_BUTTON = read_data_from_excel("HomePage", 7, 2)
    SEARCH_INPUT_BOX = read_data_from_excel("HomePage", 8, 2)
    NURSE_TRACKING = read_data_from_excel("HomePage", 9, 2)
    QUICK_APPS = read_data_from_excel("HomePage", 10, 2)
    FORMS = read_data_from_excel("HomePage", 11, 2)
    SCHOOL_PROGRAMS = read_data_from_excel("HomePage", 12, 2)