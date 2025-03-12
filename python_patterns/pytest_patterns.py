import pytest

"""
This script provides common Pytest patterns and configurations for testing in Python.

Key Concepts:
- Writing basic test functions
- Using fixtures for setup and teardown
- Parameterized testing
- Mocking with unittest.mock
- Running tests with Pytest CLI
"""

# 1. Basic Test Function
def add(a, b):
    return a + b

def test_add():
    """Test the add function with sample inputs."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# 2. Using Fixtures (Setup and Teardown)
@pytest.fixture
def sample_data():
    """Fixture providing sample test data."""
    return {"name": "Alice", "age": 30}

def test_sample_data(sample_data):
    """Test that fixture data is accessible."""
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30

# 3. Parameterized Tests
@pytest.mark.parametrize("num, expected", [(2, 4), (3, 9), (4, 16)])
def test_square(num, expected):
    """Test multiple cases using parameterized testing."""
    assert num ** 2 == expected

# 4. Mocking External Dependencies
from unittest.mock import MagicMock

def external_api():
    """Simulates an external API call."""
    return "Success"

def test_external_api(mocker):
    """Mock an external API function to control test behavior."""
    mocker.patch("__main__.external_api", return_value="Mocked Response")
    assert external_api() == "Mocked Response"

# 5. Running Tests with Pytest
"""
To run the tests, use the following commands:
- `pytest test_file.py`  -> Run all tests
- `pytest -v`  -> Run tests with detailed output
- `pytest -k "test_add"`  -> Run specific test function
- `pytest --maxfail=1`  -> Stop after first failure
- `pytest --disable-warnings`  -> Suppress warnings
"""

# Example usage (Run using pytest CLI)
if __name__ == "__main__":
    pytest.main()
