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
        """
        Initialize the WaitUtils instance with a WebDriver and an optional default timeout.

        Parameters:
        -----------
        driver : WebDriver
            The Selenium WebDriver instance.
        default_timeout : int, optional
            Default wait timeout in seconds (default is 10).
        """
        self.driver = driver
        self.default_timeout = default_timeout

    def wait_for_element(self, condition, locator, timeout=None):
        """
        Generalized method for waiting on a specific condition for an element.

        Parameters:
        -----------
        condition : expected_conditions
            The expected condition to be applied (e.g., visibility, clickability).
        locator : tuple
            Locator for the element, e.g., (By.ID, 'element_id').
        timeout : int, optional
            Timeout value in seconds (default is None, uses default_timeout).

        Returns:
        --------
        WebElement
            The WebElement that matches the condition.

        Raises:
        -------
        TimeoutException
            If the element doesn't match the condition within the specified timeout.
        """
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except TimeoutException as e:
            # Log the error, raise, or handle as needed
            raise TimeoutException(f"Element with locator {locator} not found within {timeout} seconds.") from e

    def wait_for_element_to_be_visible(self, locator, timeout=None):
        """
        Wait until the element is visible on the page.

        Parameters:
        -----------
        locator : tuple
            Locator for the element, e.g., (By.ID, 'element_id').
        timeout : int, optional
            Timeout value in seconds (default is None, uses default_timeout).

        Returns:
        --------
        WebElement
            The WebElement that is visible on the page.
        """
        return self.wait_for_element(EC.visibility_of_element_located, locator, timeout)

    def wait_for_elements_to_be_visible(self, locator, timeout=None):
        """
        Wait until all elements matching the locator are visible on the page.

        Parameters:
        -----------
        locator : tuple
            Locator for the elements, e.g., (By.CLASS_NAME, 'elements_class').
        timeout : int, optional
            Timeout value in seconds (default is None, uses default_timeout).

        Returns:
        --------
        list[WebElement]
            List of WebElements that are visible on the page.
        """
        self.wait_for_element(EC.visibility_of_all_elements_located, locator, timeout)
        return self.driver.find_elements(*locator)

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        """
        Wait until the element is clickable on the page.

        Parameters:
        -----------
        locator : tuple
            Locator for the element, e.g., (By.ID, 'element_id').
        timeout : int, optional
            Timeout value in seconds (default is None, uses default_timeout).

        Returns:
        --------
        WebElement
            The WebElement that is clickable on the page.
        """
        return self.wait_for_element(EC.element_to_be_clickable, locator, timeout)

    def wait_for_table_to_load(self, table_id, timeout=None):
        """
        Wait until the table with the specified ID is present on the page.

        Parameters:
        -----------
        table_id : str
            The ID of the table element.
        timeout : int, optional
            Timeout value in seconds (default is None, uses default_timeout).

        Returns:
        --------
        WebElement
            The table WebElement present on the page.
        """
        locator = (By.ID, table_id)
        return self.wait_for_element(EC.presence_of_element_located, locator, timeout)

    def wait_for_table_to_be_visible(self, locator, timeout=None):
        """
        Wait until the table matching the specified locator is visible on the page.

        Parameters:
        -----------
        locator : tuple
            Locator for the table element, e.g., (By.ID, 'table_id').
        timeout : int, optional
            Timeout value in seconds (default is None, uses default_timeout).

        Returns:
        --------
        WebElement
            The table WebElement that is visible on the page.
        """
        return self.wait_for_element(EC.visibility_of_element_located, locator, timeout)
