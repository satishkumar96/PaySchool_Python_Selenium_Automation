import openpyxl


def read_data_from_excel(sheetname, rownum, colnum):
    file = "C:\\Users\\SATISH\\PycharmProjects\\PaySchool_Python_Selenium_Automation\\ExcelSheet\\LocatorsValue.xlsx"
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetname]
    inputvalue = sheet.cell(row=rownum, column=colnum).value
    return inputvalue