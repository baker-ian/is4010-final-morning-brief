import pytest
from unittest.mock import patch, Mock
import sys
import os

# Add the src directory to the path so we can import the module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import your function. ADJUST THIS if your function is named differently
# or located in a different file (e.g., from main import get_weather)
from src.weather import get_weather

# Sample data that looks like a real OpenWeatherMap response
MOCK_WEATHER_DATA = {
    "weather": [{"description": "clear sky", "main": "Clear"}],
    "main": {"temp": 72.5, "humidity": 45},
    "name": "Cincinnati",
    "cod": 200
}

@patch('requests.get')
def test_get_weather_success(mock_get):
    """
    Test that get_weather successfully parses data when the API returns 200 OK.
    """
    # Configure the mock to return a successful response with our data
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = MOCK_WEATHER_DATA
    mock_get.return_value = mock_response

    # Call the function with a dummy API key
    result = get_weather("Cincinnati", "dummy_api_key")

    # Assertions based on what your function is expected to return
    # Adjust these to match your actual return format (dictionary, string, etc.)
    assert result is not None
    assert "Cincinnati" in result['city']
    assert result['temp'] == 72.5
    assert result['description'] == "clear sky"

@patch('requests.get')
def test_get_weather_api_failure(mock_get):
    """
    Test that get_weather handles API errors (e.g., 404 City Not Found) gracefully.
    """
    # Configure the mock to return a 404 error
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {"cod": "404", "message": "city not found"}
    mock_get.return_value = mock_response

    # Call the function
    result = get_weather("NotACity", "dummy_api_key")

    # Assert that the function handled the error (e.g., returned None or raised an error)
    # Adjust this based on how you decided to handle errors in your code
    assert result is None 

@patch('requests.get')
def test_get_weather_network_error(mock_get):
    """
    Test that get_weather handles network exceptions (e.g., no internet).
    """
    # Configure the mock to raise a connection error
    mock_get.side_effect = Exception("Connection refused")

    # Call the function
    result = get_weather("Cincinnati", "dummy_api_key")

    # Ensure your app doesn't crash
    assert result is None