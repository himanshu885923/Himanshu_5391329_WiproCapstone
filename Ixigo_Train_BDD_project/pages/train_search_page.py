from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from utilities.waits import waits
import time


class TrainSearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = waits(driver)

        self.from_input = (
            By.XPATH,
            "//input[@data-testid='autocompleter-input' and @placeholder='Enter Origin']"
        )

        self.from_station_option = (
            By.XPATH,
            "//p[text()='New Delhi (NDLS)']"
        )

        self.to_input = (
            By.XPATH,
            "//input[@data-testid='autocompleter-input' and @placeholder='Enter Destination']"
        )

        self.to_station_option = (
            By.XPATH,
            "//p[contains(text(),'Agra - All stations')]"
        )

        self.date_button = (
            By.XPATH,
            "//button[.//abbr[@aria-label='June 25, 2026']]"
        )

        self.search_button = (
            By.XPATH,
            "//button[@data-testid='book-train-tickets']"
        )

    def enter_from(self, city):
        field = self.wait.clickable(self.from_input)
        field.click()
        field.clear()
        field.send_keys(city)

        option = self.wait.clickable(self.from_station_option)
        self.driver.execute_script("arguments[0].click();", option)

        print("FROM selected")
        time.sleep(2)

    def enter_to(self, city):

        city = str(city).strip()

        field = self.wait.clickable(self.to_input)

        field.click()
        field.clear()
        field.send_keys(city)

        time.sleep(3)

        possible_options = [
            "//p[contains(text(),'Agra - All stations')]",
            f"//p[contains(text(),'{city}')]",
            f"//*[contains(text(),'{city}')]"
        ]

        for xpath in possible_options:

            try:
                option = self.driver.find_element(By.XPATH, xpath)

                if option.is_displayed():
                    self.driver.execute_script(
                        "arguments[0].click();",
                        option
                    )

                    print("TO selected")

                    time.sleep(2)

                    return

            except:
                pass

        # fallback keyboard selection
        field.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        field.send_keys(Keys.ENTER)

        print("TO selected using keyboard fallback")

        time.sleep(2)

    def select_date(self, travel_date):
        date = self.wait.clickable(self.date_button)
        self.driver.execute_script("arguments[0].click();", date)

        print("Date selected")
        time.sleep(2)

    def click_search(self):
        button = self.wait.clickable(self.search_button)
        self.driver.execute_script("arguments[0].click();", button)

        print("Search clicked")
        time.sleep(10)