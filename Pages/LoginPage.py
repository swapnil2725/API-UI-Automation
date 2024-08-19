import time
from selenium.webdriver.common.by import By
from config.config import TestData
from Pages.BasePage import BasePage
from config.locator import Locator


class LoginPage(BasePage):
    """
    LoginPage handles interactions with the login page of the application.

    Inherits from BasePage and utilizes its common methods for interacting
    with web elements like sending keys and clicking buttons.
    """

    def __init__(self, driver):
        """
        Constructor method to initialize the LoginPage.

        Parameters:
        -----------
        driver : WebDriver
            The Selenium WebDriver instance used to interact with the browser.
        """
        super().__init__(driver)
        self.driver.get(TestData.Base_Url)
        self.wait_for_page_to_load()

    def login_user(self, username: str = TestData.USERNAME, password: str = TestData.PASSWORD):
        """
        Logs the user into the application.

        Parameters:
        -----------
        username : str
            The username to input in the login form. Defaults to TestData.USERNAME.
        password : str
            The password to input in the login form. Defaults to TestData.PASSWORD.

        Returns:
        --------
        HomePage
            Returns an instance of the HomePage after successful login.
        """
        # Send username and password to respective input fields
        self.send_keys_to_element(Locator.USERNAME_INPUT, username)
        self.send_keys_to_element(Locator.PASSWORD_INPUT, password)

        # Click on login button
        self.do_click(Locator.LOGIN_BUTTON)

        # Wait for the home page to load and return the instance
        from Pages.HomePage import HomePage  # Avoid circular import issues
        return HomePage(self.driver)

    def is_login_page_displayed(self) -> bool:
        """
        Checks if the login page is correctly displayed.

        Returns:
        --------
        bool
            True if the login form is displayed, False otherwise.
        """
        return self.is_element_visible(Locator.LOGIN_FORM)

    def wait_for_page_to_load(self, timeout: int = TestData.TIMEOUT):
        """
        Waits for the login page to load completely.

        Parameters:
        -----------
        timeout : int
            The number of seconds to wait before timing out. Defaults to TestData.TIMEOUT.
        """
        self.wait_until_element_is_visible(Locator.LOGIN_FORM, timeout)

    def login_with_invalid_credentials(self, username: str, password: str) -> bool:
        """
        Attempts to log in with invalid credentials and verifies the error message.

        Parameters:
        -----------
        username : str
            The invalid username to test.
        password : str
            The invalid password to test.

        Returns:
        --------
        bool
            True if the error message is displayed, False otherwise.
        """
        self.login_user(username, password)
        return self.is_element_visible(Locator.ERROR_MESSAGE)



