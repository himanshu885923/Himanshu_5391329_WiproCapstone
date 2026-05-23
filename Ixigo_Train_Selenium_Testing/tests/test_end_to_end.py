import os
import time
import logging
import pytest

from utilities.excel_reader import ExcelReader

from pages.login_page import LoginPage
from pages.train_search_page import TrainSearchPage
from pages.train_results_page import TrainResultsPage
from pages.passenger_page import PassengerPage
from pages.payment_page import PaymentPage


logger = logging.getLogger(__name__)


def save_ss(driver, name):

    os.makedirs("screenshots", exist_ok=True)

    driver.save_screenshot(
        f"screenshots/{name}.png"
    )


@pytest.mark.e2e
def test_end_to_end(driver):

    logger.info("===== STARTING END TO END TEST =====")

    # Read Excel data
    data_reader = ExcelReader("testdata/test_data.xlsx")

    from_city, to_city, travel_date, name, age, gender = (
        data_reader.get_row_values()
    )

    logger.info(
        f"Test Data Loaded -> FROM: {from_city}, TO: {to_city}"
    )

    # Page Objects
    login = LoginPage(driver)
    search = TrainSearchPage(driver)
    results = TrainResultsPage(driver)
    passenger = PassengerPage(driver)
    payment = PaymentPage(driver)

    # 1. Login
    logger.info("Starting Login")

    login.login_with_phone()

    logger.info("Login completed")

    save_ss(driver, "01_login_completed")

    # 2. Click Train Icon
    logger.info("Opening Train Page")

    login.go_to_trains()

    logger.info("Train icon clicked")

    save_ss(driver, "02_train_page")

    # 3. Search Train
    logger.info("Entering FROM station")

    search.enter_from(from_city)

    logger.info("FROM selected")

    search.enter_to(to_city)

    logger.info("TO selected")

    search.select_date(travel_date)

    logger.info("Date selected")

    search.click_search()

    logger.info("Search clicked")

    time.sleep(5)

    save_ss(driver, "03_after_search")

    logger.info(
        f"After search URL: {driver.current_url}"
    )

    # 4. Select AVL Train
    logger.info("Searching AVL seats")

    results.select_available_and_book()

    logger.info("AVL seat selected and Book clicked")

    time.sleep(10)

    if len(driver.window_handles) > 1:

        driver.switch_to.window(
            driver.window_handles[-1]
        )

    logger.info(
        f"Passenger page URL: {driver.current_url}"
    )

    save_ss(driver, "04_passenger_page")

    # 5. Passenger Selection
    logger.info("Selecting Passenger")

    passenger.select_or_add_passenger(
        name,
        age,
        gender
    )

    logger.info("Passenger selected")

    time.sleep(5)

    save_ss(
        driver,
        "05_after_passenger_selection"
    )

    # 6. Payment Page
    logger.info("Proceeding to payment")

    payment.payment_page_loaded()

    logger.info(
        "Credit/Debit/ATM Card option opened"
    )

    time.sleep(5)

    save_ss(driver, "06_payment_page")

    logger.info(
        "END TO END FLOW COMPLETED SUCCESSFULLY"
    )