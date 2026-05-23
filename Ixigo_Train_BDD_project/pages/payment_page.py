from selenium.webdriver.common.by import By
from utilities.waits import waits
import time


class PaymentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = waits(driver)

        self.proceed_to_pay = (
            By.XPATH,
            "//button[contains(.,'Proceed to Pay')]"
        )

        self.insurance_yes = (
            By.XPATH,
            "//button[@data-testid='assured-popup-yes']"
        )

        self.card_xpaths = [
            "//p[text()='Credit/Debit/ATM Card']",
            "(//p[text()='Credit/Debit/ATM Card'])[1]",
            "//*[contains(text(),'Credit/Debit/ATM Card')]",
            "//*[contains(text(),'Debit')]",
            "//*[contains(text(),'Card')]"
        ]

    def payment_page_loaded(self):

        proceed = self.wait.clickable(self.proceed_to_pay)
        self.driver.execute_script("arguments[0].click();", proceed)

        print("Proceed to Pay clicked")
        time.sleep(4)

        try:
            yes = self.wait.clickable(self.insurance_yes)
            self.driver.execute_script("arguments[0].click();", yes)
            print("Insurance popup accepted")
            time.sleep(6)
        except:
            print("Insurance popup not shown")

        print("Searching Credit/Debit/ATM Card option...")

        for xpath in self.card_xpaths:

            try:
                elements = self.driver.find_elements(By.XPATH, xpath)

                for element in elements:

                    if element.is_displayed():

                        self.driver.execute_script(
                            "arguments[0].scrollIntoView({block:'center'});",
                            element
                        )

                        time.sleep(2)

                        self.driver.execute_script(
                            "arguments[0].click();",
                            element
                        )

                        print("Credit/Debit/ATM Card option clicked")

                        time.sleep(5)

                        return

            except:
                pass

        raise Exception("Credit/Debit/ATM Card option not found")