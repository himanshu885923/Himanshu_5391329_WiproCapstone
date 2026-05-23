from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config_reader import ConfigReader
import time


class HomePage:

    TRAINS_BUTTON = (
        By.XPATH,
        "/html/body/main/div[2]/div[1]/div[2]/div/ul/li[3]/a/p"
    )

    def __init__(self, driver):

        self.driver = driver

        timeout = int(ConfigReader.get("timeout"))

        self.wait = WebDriverWait(driver, timeout)

    def open_homepage(self):

        base_url = ConfigReader.get("base_url")

        self.driver.get(base_url)

        self.driver.maximize_window()

        time.sleep(5)

    def click_trains_button(self):

        trains = self.wait.until(
            EC.element_to_be_clickable(
                self.TRAINS_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            trains
        )

        time.sleep(5)