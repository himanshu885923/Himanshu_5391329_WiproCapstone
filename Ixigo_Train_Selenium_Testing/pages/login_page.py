from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.config_reader import ConfigReader
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

        self.login_button = (By.XPATH, "//*[contains(text(),'Log in') or contains(text(),'Login') or contains(text(),'Sign in')]")
        self.phone_input = (By.XPATH, "//input[contains(@placeholder,'Mobile') or contains(@placeholder,'Phone') or @type='tel']")
        self.continue_button = (By.XPATH, "//button[contains(.,'Continue') or contains(.,'Login') or contains(.,'Send OTP')]")

        self.trains_icon = (
            By.XPATH,
            "//p[contains(@class,'text-xl') and text()='Trains']"
        )

    def login_with_phone(self):
        phone = ConfigReader.get("phone_number")

        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        time.sleep(1)

        phone_box = self.wait.until(EC.element_to_be_clickable(self.phone_input))
        phone_box.clear()
        phone_box.send_keys(phone)

        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

        print("Enter OTP manually in browser.")
        time.sleep(15)
        print("OTP wait completed")

        # Wait until Trains icon appears after OTP auto-submit
        self.wait.until(
            EC.presence_of_element_located(self.trains_icon)
        )

        print("Login completed")

    def go_to_trains(self):
        train = self.wait.until(
            EC.element_to_be_clickable(self.trains_icon)
        )

        self.driver.execute_script("arguments[0].click();", train)

        print("Train icon clicked")

        time.sleep(5)