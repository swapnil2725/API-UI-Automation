import pytest
from Pages.HomePage import HomePage
from config.locator import Locator
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from config.WaitUtils import WaitUtils


@pytest.mark.usefixtures("init_driver")
class TestAutomationProject(BaseTest):
    """
    This class contains automated test cases for UI functionalities
    of the automation project.

    Methods:
    --------
    setup_method():
        Initializes required page objects and utilities before each test.

    test_ui_login():
        Tests the login functionality and subsequent actions on the home page.
    """

    def setup_method(self):
        """
        Initializes page objects and utilities for each test case.
        This method runs before each test, ensuring a fresh setup.
        """
        self.wait_utils = WaitUtils(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_ui_login(self):
        """
        Test case to validate the login process, user actions, and
        correct rendering of data on the home page.

        Steps:
        ------
        1. Log in to the application.
        2. Add a user to the system.
        3. Validate the table headers on the home page.
        4. Modify and delete user actions.
        5. Log out of the application.
        """

        # Step 1: Maximize window and log in
        self.driver.maximize_window()
        self.login_page.login_user()

        # Step 2: Initialize HomePage and perform actions
        self.home_page = HomePage(self.driver)
        self.home_page.add_user()

        # Step 3: Define expected headers for table validation
        expected_headers = [
            "Id", "Last Name", "First Name", "Dependents",
            "Salary", "Gross Pay", "Benefits Cost", "Net Pay", "Actions"
        ]

        # Verify if table headers are correctly displayed
        assert self.home_page.verify_table_headers(expected_headers), \
            "Table headers do not match the expected values."

        # Step 4: Perform other user actions like delete and modify
        self.home_page.delete_employee()
        self.home_page.modify_first_employee()

        # Step 5: Log out from the application
        self.home_page.logout()

    def teardown_method(self):
        """
        Cleanup method to perform actions after test execution,
        like closing the browser or resetting the application state if necessary.
        """
        if self.driver is not None:
            self.driver.quit()

