from unittest import TestCase

from agents.tools.weather_tools import get_weather_info


class Test(TestCase):
    def test_get_weather_info(self):
        print(get_weather_info('北京'))
