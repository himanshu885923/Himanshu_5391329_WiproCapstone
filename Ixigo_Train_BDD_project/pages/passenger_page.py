from selenium.webdriver.common.by import By
from utilities.waits import waits
import time


class PassengerPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = waits(driver)

        self.add_new_passenger = (
            By.XPATH,
            "//button[.//*[@data-testid='AddIcon'] and contains(.,'Add New passenger')]"
        )

        self.full_name = (
            By.XPATH,
            "//input[@type='text' and @name='name']"
        )

        self.age = (
            By.XPATH,
            "//input[@type='number' and @name='age']"
        )

        self.male = (
            By.XPATH,
            "//label[.//input[@value='M']]"
        )

        self.save_passenger = (
            By.XPATH,
            "//button[contains(.,'Save Passenger')]"
        )

        self.select_passengers = (
            By.XPATH,
            "//button[contains(.,'Select Passengers')]"
        )

    def select_or_add_passenger(self, name, age, gender):
        time.sleep(5)

        passenger_xpath = (
            By.XPATH,
            f"//label[.//p[text()='{name}']]"
        )

        existing = self.driver.find_elements(*passenger_xpath)

        if existing:
            print("Passenger already exists")
            self.driver.execute_script("arguments[0].click();", existing[0])

        else:
            print("Adding new passenger")

            add_btn = self.wait.clickable(self.add_new_passenger)
            self.driver.execute_script("arguments[0].click();", add_btn)
            time.sleep(3)

            name_field = self.wait.clickable(self.full_name)
            name_field.clear()
            name_field.send_keys(name)

            age_field = self.wait.clickable(self.age)
            age_field.clear()
            age_field.send_keys(str(int(float(age))))

            if str(gender).lower() == "male":
                male_btn = self.wait.clickable(self.male)
                self.driver.execute_script("arguments[0].click();", male_btn)

            save_btn = self.wait.clickable(self.save_passenger)
            self.driver.execute_script("arguments[0].click();", save_btn)

            time.sleep(5)

            passenger = self.wait.clickable(passenger_xpath)
            self.driver.execute_script("arguments[0].click();", passenger)

        select_btn = self.wait.clickable(self.select_passengers)
        self.driver.execute_script("arguments[0].click();", select_btn)

        print("Passenger selected")
        time.sleep(5)