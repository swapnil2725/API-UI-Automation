import pytest
from ApiTest.BaseClass import BaseClass
from config import BASE_URL, AUTH_TOKEN  # Importing from config.py


@pytest.fixture
def api():
    return BaseClass(AUTH_TOKEN, BASE_URL)  # Pass auth_token and base_url directly


def test_fetchingall_employees(api):
    """Test fetching all employees."""
    response = api.get_employees()
    print(response.json())  # Print response for debugging
    assert response.status_code == 200, "Expected status code to be 200"
    assert isinstance(response.json(), list), "Expected response to be a list of employees"


def test_createnew_employee(api):
    """Test creating a new employee and return its ID."""
    payload = {
        "firstName": "Test1",
        "lastName": "User1",
        "dependants": 3
    }
    response = api.create_employee(payload)
    print(response.json())  # Print response for debugging
    assert response.status_code == 200, "Expected status code to be 200"

    # Check if the response contains an ID for the newly created employee
    created_employee = response.json()
    assert isinstance(created_employee, dict), "Expected response to be a dictionary"
    assert "id" in created_employee, "Expected response to contain employee ID"
    return created_employee["id"]


def test_T003(api):
    """Test fetching an employee by ID."""
    employee_id = test_createnew_employee(api)  # Call the test to get employee ID
    response = api.get_employee_by_id(employee_id)
    print(response.json())  # Print response for debugging
    assert response.status_code == 200, "Expected status code to be 200"

    # Check if the returned employee data matches the expected ID
    employee_data = response.json()
    assert isinstance(employee_data, dict), "Expected response to be a dictionary"
    assert employee_data["id"] == employee_id, f"Expected employee ID to be {employee_id}"


def test_T004(api):
    """Test updating an existing employee."""
    employee_id = test_createnew_employee(api)  # Call the test to get employee ID
    payload = {
        "id": employee_id,
        "firstName": "Wanda",
        "lastName": "Maximoff",
        "dependants": 2
    }
    response = api.update_employee(payload)
    print(response.json())  # Print response for debugging
    assert response.status_code == 200, "Expected status code to be 200"

    # Verify that the response indicates a successful update
    updated_employee = response.json()
    assert isinstance(updated_employee, dict), "Expected response to be a dictionary"
    assert updated_employee["id"] == employee_id, f"Expected employee ID to be {employee_id}"
    assert updated_employee["firstName"] == "Wanda", "Expected first name to be 'Wanda'"
    assert updated_employee["lastName"] == "Maximoff", "Expected last name to be 'Maximoff'"
    assert updated_employee["dependants"] == 2, "Expected dependants to be 2"


def test_T005(api):
    """Test deleting an employee."""
    employee_id = test_createnew_employee(api)  # Call the test to get employee ID
    response = api.delete_employee(employee_id)
    print(response.text)  # Print raw response text for debugging
    assert response.status_code == 200, "Expected status code to be 200"