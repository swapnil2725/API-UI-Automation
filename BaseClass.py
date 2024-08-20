import requests
from config import BASE_URL, AUTH_TOKEN  # Importing from config.py

class BaseClass:
    def __init__(self, auth_token, base_url):
        self.base_url = base_url  # Just set the base URL without any additional path
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': auth_token
        }

    def get_employees(self):
        url = f"{self.base_url}/Prod/api/employees"  # Complete URL for fetching employees
        response = requests.get(url, headers=self.headers)  # Use the complete URL
        return response

    def create_employee(self, payload):
        url = f"{self.base_url}/Prod/api/employees"  # Complete URL for creating an employee
        response = requests.post(url, headers=self.headers, json=payload)
        return response

    def get_employee_by_id(self, employee_id):
        url = f"{self.base_url}/Prod/api/employees/{employee_id}"  # Complete URL for fetching employee by ID
        response = requests.get(url, headers=self.headers)
        return response

    def update_employee(self, payload):
        url = f"{self.base_url}/Prod/api/employees"  # Complete URL for updating an employee
        response = requests.put(url, headers=self.headers, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response

    def delete_employee(self, employee_id):
        url = f"{self.base_url}/Prod/api/employees/{employee_id}"  # Complete URL for deletion
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()  # Ensure we raise an error for bad responses
        return response