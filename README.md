# MyObservatory Test Automation

## Overview

This file with instructions on setting up the environment, installing dependencies, and running the tests.

## Set up environment

- Python 3.9
- Appium server
- Android Emulator or iOS Simulator or connect real device
- Change desired_caps for iOS or Android

## Dependencies

1. Install Poetry:
   You can follow the instructions at Poetry's official website (https://python-poetry.org/docs/#installation).

2. Clone the repository:
   git clone https://github.com/edwinlaw-git/Question2.git

## Run the tests
   
1. Start the Appium server.

2. Run the tests using Poetry.
poetry run pytest tests/test_weather_forecast.py
