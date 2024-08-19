from selenium.webdriver.common.by import By


class Locator:
    """ login page locator"""
    USERNAME_INPUT = (By.ID, "Username")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH,"//*[@action='/Prod/Account/LogIn']//*[@xpath='1']")
    LOGIN_FORM = (By.XPATH,"//*[@class='container']//*[contains(text(),'Paylocity Benefits Dashboard')]")

    """ home page Locator"""
    addUser = (By.ID, "add")
    FirstName = (By.ID, "firstName")
    LastName = (By.ID, "lastName")
    Dependents = (By.ID, "dependants")
    addEmployee = (By.ID, "addEmployee")
    #employees_table = (By.ID, "employeesTable")
    employees_table = (By.CSS_SELECTOR, "#employeesTable thead th")
    logout = (By.XPATH, "//a[contains(text(),'Log Out')]")
    delete = (By.XPATH, "//*[@id='employeesTable']/tbody/tr[last()-1]/td[9]/i[2]")
    delete_modal_id =(By.ID, "deleteModal")
    confirm_delete_button = (By.ID, "deleteEmployee")
    employees_table_id = (By.ID, "employeesTable")  # Ensure this is correctly defined
    row = (By.CSS_SELECTOR, "#employeesTable tbody tr")
    modify =  (By.XPATH, "//tbody/tr[1]/td[9]/i[1]")
    modifyEmployee = (By.ID, "updateEmployee")



