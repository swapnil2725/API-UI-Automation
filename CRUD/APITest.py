import pytest
from CRUD.BaseClass import BaseAPIClient
from CRUD.config import  Config # Importing from config.py


@pytest.fixture(scope='module')
def api_client():
    """Fixture for creating a BaseAPIClient instance."""
    client = BaseAPIClient(Config.AUTH_TOKEN, Config.BASE_URL)
    yield client



@pytest.fixture
def employee_data():
    """Fixture providing sample employee data for testing."""
    return {
        "firstName": "Test1",
        "lastName": "User1",
        "dependants": 3
    }


@pytest.fixture
def new_employee(api_client, employee_data):
    """Fixture for creating a new employee and returning its ID."""
    response = api_client.create_employee(employee_data)
    assert response.status_code == 200, "Expected status code to be 200"
    created_employee = response.json()
    assert isinstance(created_employee, dict), "Expected response to be a dictionary"
    assert "id" in created_employee, "Expected response to contain employee ID"
    return created_employee["id"]


def test_get_all_employees(api_client):
    """Test fetching all employees."""
    response = api_client.get_employees()
    assert response.status_code == 200, "Expected status code to be 200"
    assert isinstance(response.json(), list), "Expected response to be a list of employees"


def test_create_new_employee(api_client, employee_data):
    """Test creating a new employee and returning its ID."""
    response = api_client.create_employee(employee_data)
    assert response.status_code == 200, "Expected status code to be 200"
    created_employee = response.json()
    assert isinstance(created_employee, dict), "Expected response to be a dictionary"
    assert "id" in created_employee, "Expected response to contain employee ID"
    return created_employee["id"]


def test_get_employee_by_id(api_client, new_employee, employee_data):
    """Test fetching an employee by ID."""
    response = api_client.get_employee_by_id(new_employee)
    assert response.status_code == 200, "Expected status code to be 200"
    employee_data = response.json()
    assert isinstance(employee_data, dict), "Expected response to be a dictionary"
    assert employee_data["id"] == new_employee, f"Expected employee ID to be {new_employee}"


def test_update_existing_employee(api_client, new_employee):
    """Test updating an existing employee."""
    payload = {
        "id": new_employee,
        "firstName": "Wanda",
        "lastName": "Maximoff",
        "dependants": 2
    }
    response = api_client.update_employee(payload)
    assert response.status_code == 200, "Expected status code to be 200"
    updated_employee = response.json()
    assert isinstance(updated_employee, dict), "Expected response to be a dictionary"
    assert updated_employee["id"] == new_employee, f"Expected employee ID to be {new_employee}"
    assert updated_employee["firstName"] == "Wanda", "Expected first name to be 'Wanda'"
    assert updated_employee["lastName"] == "Maximoff", "Expected last name to be 'Maximoff'"
    assert updated_employee["dependants"] == 2, "Expected dependants to be 2"


def test_delete_employee(api_client, new_employee):
    """Test deleting an employee."""
    response = api_client.delete_employee(new_employee)
    assert response.status_code == 200, "Expected status code to be 200"
