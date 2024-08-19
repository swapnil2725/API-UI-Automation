import os


class Config:
    """Configuration class to hold configuration variables."""

    # Base URL for API endpoints
    BASE_URL = os.getenv('BASE_URL', 'https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com')

    # Authentication token for API requests
    AUTH_TOKEN = os.getenv('AUTH_TOKEN', 'Basic VGVzdFVzZXI0MDQ6Z1BpK0U2KjE4VypX')


    @classmethod
    def display_config(cls):
        """Display the current configuration."""
        print("Current Configuration:")
        print(f"BASE_URL: {cls.BASE_URL}")
        print(f"AUTH_TOKEN: {cls.AUTH_TOKEN}")


# Example usage:
if __name__ == "__main__":
    Config.display_config()
    Config.display_config()