from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TrainResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def select_available_and_book(self):

        print("Searching any AVL seat card...")

        avl_cards_xpath = "//div[contains(@class,'_avail-card') and .//*[contains(text(),'AVL')]]"

        for scroll in range(10):

            avl_cards = self.driver.find_elements(By.XPATH, avl_cards_xpath)

            for card in avl_cards:

                try:
                    if card.is_displayed():

                        self.driver.execute_script(
                            "arguments[0].scrollIntoView({block:'center'});",
                            card
                        )

                        time.sleep(2)

                        print("Clicking AVL card:", card.text)

                        self.driver.execute_script(
                            "arguments[0].click();",
                            card
                        )

                        time.sleep(3)

                        print("Searching Book button near selected AVL...")

                        book_buttons = self.driver.find_elements(
                            By.XPATH,
                            "//button[.//span[normalize-space()='Book'] or contains(.,'Book')]"
                        )

                        for button in book_buttons:

                            try:
                                if button.is_displayed() and button.is_enabled():

                                    self.driver.execute_script(
                                        "arguments[0].scrollIntoView({block:'center'});",
                                        button
                                    )

                                    time.sleep(1)

                                    print("Clicking Book button:", button.text)

                                    self.driver.execute_script(
                                        "arguments[0].click();",
                                        button
                                    )

                                    time.sleep(10)

                                    return

                            except:
                                pass

                except:
                    pass

            self.driver.execute_script("window.scrollBy(0,700);")
            time.sleep(2)

        raise Exception("No AVL card with visible Book button found")