import os
import pytest
import time
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.train_search_page import TrainSearchPage
from pages.train_results_page import TrainResultsPage
from pages.passenger_page import PassengerPage
from pages.payment_page import PaymentPage
from utilities.excel_reader import ExcelReader


def save_ss(driver, name):
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(f"screenshots/{name}.png")


@pytest.mark.positive
def test_01_login_and_train_icon(driver):
    login = LoginPage(driver)

    login.login_with_phone()
    save_ss(driver, "test_01_login_completed")

    train_icon = driver.find_element(
        By.XPATH,
        "//p[contains(@class,'text-xl') and text()='Trains']"
    )

    assert train_icon.is_displayed(), "Train icon is not visible after login"
    print("PASSED: Login successful and Train icon visible")


@pytest.mark.positive
def test_02_train_search_with_valid_data(driver):
    data_reader = ExcelReader("testdata/test_data.xlsx")
    from_city, to_city, travel_date, name, age, gender = data_reader.get_row_values()

    login = LoginPage(driver)
    search = TrainSearchPage(driver)

    login.login_with_phone()
    login.go_to_trains()

    search.enter_from(from_city)
    search.enter_to(to_city)
    search.select_date(travel_date)
    search.click_search()

    time.sleep(5)
    save_ss(driver, "test_02_train_search")

    assert "search-pwa/from" in driver.current_url, "Train search result page not opened"
    print("PASSED: Valid train search completed")


@pytest.mark.positive
def test_03_available_ticket_and_book(driver):
    data_reader = ExcelReader("testdata/test_data.xlsx")
    from_city, to_city, travel_date, name, age, gender = data_reader.get_row_values()

    login = LoginPage(driver)
    search = TrainSearchPage(driver)
    results = TrainResultsPage(driver)

    login.login_with_phone()
    login.go_to_trains()

    search.enter_from(from_city)
    search.enter_to(to_city)
    search.select_date(travel_date)
    search.click_search()

    results.select_available_and_book()

    time.sleep(5)
    save_ss(driver, "test_03_after_book")

    assert "passenger-details" in driver.current_url, "Passenger page not opened after Book"
    print("PASSED: Available seat selected and Book clicked")


@pytest.mark.positive
def test_04_passenger_and_payment_page(driver):
    data_reader = ExcelReader("testdata/test_data.xlsx")
    from_city, to_city, travel_date, name, age, gender = data_reader.get_row_values()

    login = LoginPage(driver)
    search = TrainSearchPage(driver)
    results = TrainResultsPage(driver)
    passenger = PassengerPage(driver)
    payment = PaymentPage(driver)

    login.login_with_phone()
    login.go_to_trains()

    search.enter_from(from_city)
    search.enter_to(to_city)
    search.select_date(travel_date)
    search.click_search()

    results.select_available_and_book()

    time.sleep(5)

    passenger.select_or_add_passenger(name, age, gender)

    payment.payment_page_loaded()

    time.sleep(5)

    save_ss(driver, "test_04_card_payment_option_clicked")

    page_text = driver.page_source.lower()

    assert (
        "card" in page_text
        or "credit" in page_text
        or "debit" in page_text
        or "atm" in page_text
    ), "Credit/Debit/ATM Card option was not opened"

    print("PASSED: Passenger selected and Credit/Debit/ATM Card option opened")


@pytest.mark.negative
def test_05_invalid_from_station_validation(driver):
    login = LoginPage(driver)

    login.login_with_phone()
    login.go_to_trains()

    from_input = driver.find_element(
        By.XPATH,
        "//input[@data-testid='autocompleter-input' and @placeholder='Enter Origin']"
    )

    from_input.click()
    from_input.clear()
    from_input.send_keys("INVALID123")

    time.sleep(4)
    save_ss(driver, "test_05_invalid_station")

    page_text = driver.page_source.lower()

    assert (
        "no matching station" in page_text
        or "try a different spelling" in page_text
        or "invalid" in page_text
        or len(driver.find_elements(By.XPATH, "//p[contains(text(),'INVALID123')]")) == 0
    ), "Invalid station was accepted"

    print("PASSED: Invalid station validation working")


@pytest.mark.negative
def test_06_empty_passenger_name_validation(driver):
    data_reader = ExcelReader("testdata/test_data.xlsx")
    from_city, to_city, travel_date, name, age, gender = data_reader.get_row_values()

    login = LoginPage(driver)
    search = TrainSearchPage(driver)
    results = TrainResultsPage(driver)

    login.login_with_phone()
    login.go_to_trains()

    search.enter_from(from_city)
    search.enter_to(to_city)
    search.select_date(travel_date)
    search.click_search()

    results.select_available_and_book()
    time.sleep(5)

    add_btn = driver.find_element(
        By.XPATH,
        "//button[.//*[@data-testid='AddIcon'] and contains(.,'Add New passenger')]"
    )
    driver.execute_script("arguments[0].click();", add_btn)

    time.sleep(2)

    age_field = driver.find_element(
        By.XPATH,
        "//input[@type='number' and @name='age']"
    )
    age_field.send_keys("18")

    male = driver.find_element(
        By.XPATH,
        "//label[.//input[@value='M']]"
    )
    driver.execute_script("arguments[0].click();", male)

    save_btn = driver.find_element(
        By.XPATH,
        "//button[contains(.,'Save Passenger')]"
    )
    driver.execute_script("arguments[0].click();", save_btn)

    time.sleep(3)
    save_ss(driver, "test_06_empty_passenger_name")

    assert "passenger-details" in driver.current_url, "Passenger saved with empty name"
    print("PASSED: Empty passenger name validation working")