from selenium.webdriver.common.by import By
from config.config import TestData
from Pages.BasePage import BasePage
from config.locator import Locator
from config.WaitUtils import WaitUtils


class HomePage(BasePage):
    """
    HomePage class representing the actions and verifications that can be performed
    on the application's home page, such as adding, modifying, and deleting employees.
    """

    def __init__(self, driver):
        """
        Initialize HomePage with WebDriver and utilities.

        Parameters:
        -----------
        driver : WebDriver
            The WebDriver instance to interact with the page.
        """
        super().__init__(driver)
        self.wait_utils = WaitUtils(driver)

    def add_user(self, first_name="Test1", last_name="User1", dependents="3"):
        """
        Add a user with the provided details.

        Parameters:
        -----------
        first_name : str, optional
            First name of the user (default is "Test1").
        last_name : str, optional
            Last name of the user (default is "User1").
        dependents : str, optional
            Number of dependents (default is "3").
        """
        self.wait_utils.wait_for_element_to_be_clickable(Locator.addUser)
        self.do_click(Locator.addUser)

        self.send_keys_to_element(Locator.FirstName, first_name)
        self.send_keys_to_element(Locator.LastName, last_name)
        self.send_keys_to_element(Locator.Dependents, dependents)

        self.wait_utils.wait_for_element_to_be_clickable(Locator.addEmployee)
        self.do_click(Locator.addEmployee)

    def verify_table_headers(self, expected_headers):
        """
        Verify if the actual table headers match the expected headers.

        Parameters:
        -----------
        expected_headers : list
            A list of expected header names.

        Raises:
        -------
        AssertionError
            If the actual headers do not match the expected headers.
        """
        headers = self.wait_utils.wait_for_elements_to_be_visible(Locator.employees_table)
        actual_headers = [header.text.strip() for header in headers]

        assert actual_headers == expected_headers, \
            f"Expected headers: {expected_headers}, but found: {actual_headers}"

    def delete_employee(self):
        """
        Delete an employee by clicking the delete button and confirming the action.
        """
        self.wait_utils.wait_for_element_to_be_clickable(Locator.delete)
        self.do_click(Locator.delete)

        self.wait_utils.wait_for_element_to_be_clickable(Locator.confirm_delete_button)
        self.do_click(Locator.confirm_delete_button)

    def modify_first_employee(self, first_name="Random", last_name="User112", dependents="3"):
        """
        Modify the details of the first employee.

        Parameters:
        -----------
        first_name : str, optional
            The new first name for the employee (default is "Random").
        last_name : str, optional
            The new last name for the employee (default is "User112").
        dependents : str, optional
            The new number of dependents (default is "3").
        """
        self.wait_utils.wait_for_element_to_be_clickable(Locator.modify)
        self.do_click(Locator.modify)

        self.clear_and_send_keys(Locator.FirstName, first_name)
        self.clear_and_send_keys(Locator.LastName, last_name)
        self.clear_and_send_keys(Locator.Dependents, dependents)

        self.wait_utils.wait_for_element_to_be_clickable(Locator.modifyEmployee)
        self.do_click(Locator.modifyEmployee)

    def logout(self):
        """
        Log out from the application.
        """
        self.wait_utils.wait_for_element_to_be_clickable(Locator.logout)
        self.do_click(Locator.logout)

    def clear_and_send_keys(self, locator, text):
        """
        Clear the input field and then send the specified keys to it.

        Parameters:
        -----------
        locator : By
            The locator of the element.
        text : str
            The text to be sent to the input field.
        """
        element = self.wait_utils.wait_for_element_to_be_visible(locator)
        element.clear()
        element.send_keys(text)





