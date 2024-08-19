import requests
from requests.exceptions import HTTPError, RequestException
import logging

class BaseAPIClient:
    def __init__(self, base_url: str, auth_token: str):
        """
        Initialize the API client with base URL and authentication token.

        :param base_url: The base URL for API requests.
        :param auth_token: The authentication token for API requests.
        """
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {auth_token}"
        }
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def _handle_response(self, response: requests.Response):
        """
        Handle HTTP responses, logging and raising exceptions if needed.

        :param response: The HTTP response object.
        :raises HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        try:
            response.raise_for_status()
        except HTTPError as http_err:
            self.logger.error(f"HTTP error occurred: {http_err}")
            raise
        except RequestException as req_err:
            self.logger.error(f"Request error occurred: {req_err}")
            raise
        else:
            self.logger.info(f"Response received: {response.status_code}")
            return response

    def get_employees(self):
        """
        Fetch the list of employees from the API.

        :return: The HTTP response object.
        """
        url = f"{self.base_url}/Prod/api/employees"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def create_employee(self, payload: dict):
        """
        Create a new employee with the given payload.

        :param payload: The data to be sent in the request body.
        :return: The HTTP response object.
        """
        url = f"{self.base_url}/Prod/api/employees"
        response = requests.post(url, headers=self.headers, json=payload)
        return self._handle_response(response)

    def get_employee_by_id(self, employee_id: str):
        """
        Retrieve an employee's details by their ID.

        :param employee_id: The ID of the employee to retrieve.
        :return: The HTTP response object.
        """
        url = f"{self.base_url}/Prod/api/employees/{employee_id}"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def update_employee(self, employee_id: str, payload: dict):
        """
        Update an existing employee's information.

        :param employee_id: The ID of the employee to update.
        :param payload: The data to be sent in the request body.
        :return: The HTTP response object.
        """
        url = f"{self.base_url}/Prod/api/employees/{employee_id}"
        response = requests.put(url, headers=self.headers, json=payload)
        return self._handle_response(response)

    def delete_employee(self, employee_id: str):
        """
        Delete an employee by their ID.

        :param employee_id: The ID of the employee to delete.
        :return: The HTTP response object.
        """
        url = f"{self.base_url}/Prod/api/employees/{employee_id}"
        response = requests.delete(url, headers=self.headers)
        return self._handle_response(response)

