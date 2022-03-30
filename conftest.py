import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# For Chromium
from webdriver_manager.utils import ChromeType


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--start-in-incognito")

    # For Chrome
    # service=Service(ChromeDriverManager().install())

    # For Chromium
    service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    driver = webdriver.Chrome(service=service, options=options)
    
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
