import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Uncomment this if you want to run tests headlessly
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Correctly setting up Chrome driver with options
        chrome_driver_path = ChromeDriverManager().install()
        service = ChromeService(executable_path=chrome_driver_path)
        web_driver = webdriver.Chrome(service=service, options=chrome_options)

    request.cls.driver = web_driver
    yield
    web_driver.quit()