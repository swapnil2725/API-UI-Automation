Running the Tests
To run the tests, follow these steps:

1. Install Dependencies: Ensure you have pytest and any other required libraries installed. You can install them using pip:

      `pip install pytest requests`

2. Set Up Environment Variables: Make sure BASE_URL and AUTH_TOKEN are set in your environment. You can set them directly in your terminal or use a .env file with python-dotenv.
3. Run Tests: Execute the tests using pytest:
      `pytest {FileName}`

Additional Information
BaseAPIClient: The BaseAPIClient class should handle the actual API requests. Ensure it implements methods like get_employees, create_employee, get_employee_by_id, update_employee, and delete_employee.
