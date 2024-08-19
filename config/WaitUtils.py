from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class WaitUtils:
    """
    WaitUtils class provides utility methods for waiting on web elements
    to be visible, clickable, or present on the page using WebDriverWait.

    Attributes:
    -----------
    driver : WebDriver
        The Selenium WebDriver instance used for performing actions and locating elements.
    default_timeout : int
        The default timeout value (in seconds) for wait operations.
    """

    def __init__(self, driver, default_timeout=10):

        self.driver = driver
        self.default_timeout = default_timeout

    def wait_for_element(self, condition, locator, timeout=None):

        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except TimeoutException as e:
            # Log the error, raise, or handle as needed
            raise TimeoutException(f"Element with locator {locator} not found within {timeout} seconds.") from e

    def wait_for_element_to_be_visible(self, locator, timeout=None):

        return self.wait_for_element(EC.visibility_of_element_located, locator, timeout)

    def wait_for_elements_to_be_visible(self, locator, timeout=None):

        self.wait_for_element(EC.visibility_of_all_elements_located, locator, timeout)
        return self.driver.find_elements(*locator)

    def wait_for_element_to_be_clickable(self, locator, timeout=None):

        return self.wait_for_element(EC.element_to_be_clickable, locator, timeout)

    def wait_for_table_to_load(self, table_id, timeout=None):

        locator = (By.ID, table_id)
        return self.wait_for_element(EC.presence_of_element_located, locator, timeout)

    def wait_for_table_to_be_visible(self, locator, timeout=None):

        return self.wait_for_element(EC.visibility_of_element_located, locator, timeout)
