import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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

        super().__init__(driver)
        self.driver.get(TestData.Base_Url)
        self.wait_for_page_to_load()

    def login_user(self, username: str = TestData.USERNAME, password: str = TestData.PASSWORD):

        # Send username and password to respective input fields
        self.send_keys_to_element(Locator.USERNAME_INPUT, username)
        self.send_keys_to_element(Locator.PASSWORD_INPUT, password)

        # Click on login button
        self.do_click(Locator.LOGIN_BUTTON)

        # Wait for the home page to load and return the instance
        from Pages.HomePage import HomePage  # Avoid circular import issues
        return HomePage(self.driver)

    def is_login_page_displayed(self) -> bool:


        return self.is_element_visible(Locator.LOGIN_FORM)

    def wait_for_page_to_load(self, timeout: int = TestData.TIMEOUT):

        self.wait_until_element_is_visible(Locator.LOGIN_FORM, timeout)

    def login_with_invalid_credentials(self, username: str, password: str) -> bool:

        self.login_user(username, password)
        return self.is_element_visible(Locator.ERROR_MESSAGE)

    def wait_until_element_is_visible(self, by_locator, timeout):

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(Locator.LOGIN_FORM))
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, by_locator, timeout):

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(Locator.LOGIN_BUTTON))
            return True
        except TimeoutException:
            return False





