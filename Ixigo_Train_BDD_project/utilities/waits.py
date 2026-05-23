from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class waits:

    def __init__(self, driver, timeout=20):

        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def clickable(self, locator):

        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )