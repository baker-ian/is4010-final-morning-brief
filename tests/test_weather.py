import pytest
from unittest.mock import patch, Mock
import sys
import os
import requests  # <--- NEW IMPORT NEEDED

# Ensure we can find the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["WEATHER_API_KEY"] = "test"
from src.weather import get_weather

MOCK_WEATHER_DATA = {
    "weather": [{"description": "clear sky", "main": "Clear"}],
    "main": {"temp": 72.5, "humidity": 45},
    "name": "Cincinnati",
    "cod": 200
}

@patch('src.weather.requests.get')
def test_get_weather_success(mock_get):
    """Test that get_weather successfully parses data when the API returns 200 OK."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = MOCK_WEATHER_DATA
    mock_get.return_value = mock_response

    result = get_weather("Cincinnati")

    assert result is not None
    assert result['city'] == "Cincinnati"
    assert result['temp'] == 72.5

@patch('src.weather.requests.get')
def test_get_weather_api_failure(mock_get):
    """Test that get_weather handles API errors (e.g., 404 City Not Found) gracefully."""
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {"cod": "404", "message": "city not found"}
    mock_get.return_value = mock_response

    result = get_weather("NotACity")

    assert result is not None
    assert "error" in result
    assert "not found" in result["error"]

@patch('src.weather.requests.get')
def test_get_weather_network_error(mock_get):
    """Test that get_weather handles network exceptions (e.g., no internet)."""
    
    # FIX: Raise a specific RequestException, not a generic Exception
    mock_get.side_effect = requests.exceptions.ConnectionError("Connection refused")

    result = get_weather("Cincinnati")

    assert result is not None
    assert "error" in result
    assert "Connection Error" in result["error"]