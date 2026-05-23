from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def get_driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver_path = os.path.join(
        os.getcwd(),
        "drivers",
        "chromedriver_148_mac_arm64"
    )

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver
