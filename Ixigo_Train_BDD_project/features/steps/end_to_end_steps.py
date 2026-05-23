import time
from behave import given, when, then
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.train_search_page import TrainSearchPage
from pages.train_results_page import TrainResultsPage
from pages.passenger_page import PassengerPage
from pages.payment_page import PaymentPage
from utilities.excel_reader import ExcelReader


@given("user opens ixigo website")
def step_open_ixigo(context):
    assert "ixigo" in context.driver.title.lower()


@when("user logs in using phone number and otp")
def step_login(context):
    context.login = LoginPage(context.driver)
    context.login.login_with_phone()


@when("user clicks on trains icon")
def step_click_train(context):
    context.login.go_to_trains()


@when("user searches train using excel data")
def step_search_train(context):
    data_reader = ExcelReader("testdata/test_data.xlsx")
    from_city, to_city, travel_date, name, age, gender = data_reader.get_row_values()

    context.name = name
    context.age = age
    context.gender = gender

    context.search = TrainSearchPage(context.driver)
    context.search.enter_from(from_city)
    context.search.enter_to(to_city)
    context.search.select_date(travel_date)
    context.search.click_search()

    time.sleep(5)


@when("user selects available seat and clicks book")
def step_select_book(context):
    context.results = TrainResultsPage(context.driver)
    context.results.select_available_and_book()

    time.sleep(5)

    if len(context.driver.window_handles) > 1:
        context.driver.switch_to.window(context.driver.window_handles[-1])


@when("user selects or adds passenger")
def step_select_passenger(context):
    context.passenger = PassengerPage(context.driver)
    context.passenger.select_or_add_passenger(
        context.name,
        context.age,
        context.gender
    )


@when("user proceeds to payment")
def step_payment(context):
    context.payment = PaymentPage(context.driver)
    context.payment.payment_page_loaded()


@then("payment page should be displayed")
def step_payment_displayed(context):
    page_text = context.driver.page_source.lower()

    assert (
        "payment" in page_text
        or "card" in page_text
        or "pay" in page_text
    )