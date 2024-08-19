from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.WaitUtils import WaitUtils

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    BasePage encapsulates common web interactions with a Selenium WebDriver.

    Attributes:
    -----------
    driver : WebDriver
        Selenium WebDriver instance for browser interaction.
    waitUtils : WaitUtils
        Utility class for handling wait conditions.

    Methods:
    --------
    do_click(by_locator):
        Clicks an element identified by the given locator.

    do_page_scroll(by_locator):
        Scrolls the page to an element identified by the locator.

    send_keys_to_element(by_locator, keys):
        Sends a string of keys to an element.

    clear(by_locator):
        Clears text from an input element identified by the locator.

    get_table_rows(locator):
        Returns rows from the table identified by the locator.
    """

    def __init__(self, driver):
        self.driver = driver
        self.waitUtils = WaitUtils(driver)  # Instance of utility class for explicit waits
        self.logger = logging.getLogger(__name__)  # Initialize logger for the class

    def do_click(self, by_locator):

        try:
            element = self.waitUtils.wait_for_element_to_be_clickable(by_locator)
            element.click()
            self.logger.info(f"Clicked on the element located by {by_locator}.")
        except Exception as e:
            self.logger.error(f"Failed to click on element located by {by_locator}. Error: {str(e)}")
            raise

    def do_page_scroll(self, by_locator):

        try:
            element = self.waitUtils.wait_for_element_to_be_visible(by_locator)
            element.send_keys(Keys.END)
            self.logger.info(f"Scrolled the page to the element located by {by_locator}.")
        except Exception as e:
            self.logger.error(f"Failed to scroll to the element located by {by_locator}. Error: {str(e)}")
            raise

    def send_keys_to_element(self, by_locator, keys):

        try:
            element = self.waitUtils.wait_for_element_to_be_visible(by_locator)
            element.send_keys(keys)
            self.logger.info(f"Sent keys to the element located by {by_locator}.")
        except Exception as e:
            self.logger.error(f"Failed to send keys to element located by {by_locator}. Error: {str(e)}")
            raise

    def clear(self, by_locator):

        try:
            element = self.waitUtils.wait_for_element_to_be_clickable(by_locator)
            element.clear()
            self.logger.info(f"Cleared text from the input element located by {by_locator}.")
        except Exception as e:
            self.logger.error(f"Failed to clear the input element located by {by_locator}. Error: {str(e)}")
            raise

    def get_table_rows(self, locator):

        try:
            table = self.waitUtils.wait_for_table_to_load(locator)
            rows = table.find_elements(By.XPATH, ".//tbody/tr")
            self.logger.info(f"Retrieved {len(rows)} rows from the table located by {locator}.")
            return rows
        except Exception as e:
            self.logger.error(f"Failed to retrieve rows from the table located by {locator}. Error: {str(e)}")
            raise


