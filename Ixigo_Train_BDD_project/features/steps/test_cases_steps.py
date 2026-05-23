import time
from behave import then, when
from selenium.webdriver.common.by import By


@then("trains icon should be visible")
def step_train_icon_visible(context):
    train_icon = context.driver.find_element(
        By.XPATH,
        "//p[contains(@class,'text-xl') and text()='Trains']"
    )

    assert train_icon.is_displayed()


@then("train result page should open")
def step_result_page_open(context):
    assert "search-pwa/from" in context.driver.current_url


@then("passenger page should open")
def step_passenger_page_open(context):
    assert "passenger-details" in context.driver.current_url


@when("user enters invalid from station")
def step_invalid_station(context):
    from_input = context.driver.find_element(
        By.XPATH,
        "//input[@data-testid='autocompleter-input' and @placeholder='Enter Origin']"
    )

    from_input.click()
    from_input.clear()
    from_input.send_keys("INVALID123")

    time.sleep(4)


@then("invalid station should not be accepted")
def step_invalid_station_assert(context):
    page_text = context.driver.page_source.lower()

    assert (
        "no matching station" in page_text
        or "try a different spelling" in page_text
        or "invalid" in page_text
        or len(context.driver.find_elements(By.XPATH, "//p[contains(text(),'INVALID123')]")) == 0
    )


@when("user tries to save passenger without name")
def step_empty_passenger(context):
    add_btn = context.driver.find_element(
        By.XPATH,
        "//button[.//*[@data-testid='AddIcon'] and contains(.,'Add New passenger')]"
    )

    context.driver.execute_script("arguments[0].click();", add_btn)

    time.sleep(2)

    age_field = context.driver.find_element(
        By.XPATH,
        "//input[@type='number' and @name='age']"
    )

    age_field.send_keys("18")

    male = context.driver.find_element(
        By.XPATH,
        "//label[.//input[@value='M']]"
    )

    context.driver.execute_script("arguments[0].click();", male)

    save_btn = context.driver.find_element(
        By.XPATH,
        "//button[contains(.,'Save Passenger')]"
    )

    context.driver.execute_script("arguments[0].click();", save_btn)

    time.sleep(3)


@then("passenger should not be saved")
def step_empty_passenger_assert(context):
    assert "passenger-details" in context.driver.current_url