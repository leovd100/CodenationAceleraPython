from main import get_temperature
from unittest.mock import patch
import pytest


def test_get_temperature_by_lat_lng():
	mock_get_patcher = patch('main.requests.get')

	lat = -14.235004
	lng = -51.92528

	temperature = {
		"currently" : {
			"temperature" : 62
		}

	}
	mock_get = mock_get_patcher.start()

	mock_get.return_value.json.return_value = temperature


	resposta = get_temperature(lat,lng)

	mock_get.stop()

	assert resposta == 16 
