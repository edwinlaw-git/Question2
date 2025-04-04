import time
import datetime
from appium import webdriver
import pytest

# Set up the desired_caps for appium session
desired_caps = {
        "platformName": "Android",  # or "iOS"
        "deviceName": "Android Emulator",
        "appPackage": "hk.gov.hko.myobservatory",
        "appActivity": "hk.gov.hko.myobservatory.ui.MainActivity",
        "noReset": True,
        }

@pytest.fixture(scope='module')
def driver():
    # Start the Appium server
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()

def test_weather_forecast(driver):
    # Navigate to 9-day forecast
    time.sleep(5)
    menu_button = driver.find_element("xpath", "//android.widget.Button[@content-desc='menu']")
    menu_button.click()
    forecast_button = driver.find_element("xpath", "//android.widget.Button[@content-desc='9-Day Forecast']")
    forecast_button.click()
    time.sleep(3)

 
    first_day_forecast = driver.find_element("xpath", "//android.widget.TextView[@index='0']")  # Use the correct locator
    forecast_date_text = first_day_forecast.text
    
    forecast_date = forecast_date_text.split()[0]
    
    # Get today's date
    expected_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Verify that the date is correct
    assert forecast_date == expected_date, f"Expected date {expected_date}, but got {forecast_date}"

    print(f"Verification successful: Forecast date is {forecast_date}.")