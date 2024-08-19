class TestData:
    """
    TestData class contains configuration data and constants for tests.

    Attributes:
    -----------
    Base_Url : str
        The base URL for the API endpoint or UI test.
    """

    # Base URL for the application under test (UI or API)
    Base_Url: str = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/LogIn"


    TIMEOUT = 30  # Default timeout for UI/API waits (in seconds)
    RETRY_COUNT = 3  # Number of retries for failed tests before final assertion
    HEADERS: dict = {"Content-Type": "application/json"}  # Default headers for API tests


    USERNAME: str = "TestUser404"
    PASSWORD: str = "gPi+E6*18W*W"
