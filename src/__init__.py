"""
Morning Brief Package
---------------------
A CLI tool to fetch weather and daily briefings.
"""

# Assuming you have a weather.py file with a get_weather function
# and a main.py file with a main function.
# ADJUST THESE IMPORTS if your file names are different.

try:
    from .weather import get_weather
except ImportError:
    # This handles cases where dependencies might not be installed yet
    pass

__version__ = "0.1.0"
__author__ = "Ian Baker"