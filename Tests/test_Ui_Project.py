from Pages.HomePage import HomePage
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from config.WaitUtils import WaitUtils


class Test_Automation_Project(BaseTest):
    def setup_method(self):
        # Initialize the LoginPage instance here
        self.waitUtils = WaitUtils(self.driver)
        self.loginPage = LoginPage(self.driver)

    def test_Ui_Login(self):
        self.driver.maximize_window()
        self.loginPage.login_user()

        self.homePage = HomePage(self.driver)
        self.homePage.add_user()
        expected_headers = [
            "Id",
            "Last Name",
            "First Name",
            "Dependents",
            "Salary",
            "Gross Pay",
            "Benefits Cost",
            "Net Pay",
            "Actions"
        ]

        # Verify table headers
        self.homePage.verify_table_headers(expected_headers)

        self.homePage.delete_employee()

        self.homePage.modify_first_employee()

        self.homePage.logout()
