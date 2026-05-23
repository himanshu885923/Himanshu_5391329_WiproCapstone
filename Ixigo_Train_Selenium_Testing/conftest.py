import os
import time
import shutil
import subprocess
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.config_reader import ConfigReader


@pytest.fixture(scope="function")
def driver():

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    base_url = ConfigReader.get("base_url")
    driver.get(base_url)

    time.sleep(5)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        driver = item.funcargs.get("driver")

        if driver:

            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            status = "PASSED" if report.passed else "FAILED"

            screenshot_path = os.path.join(
                screenshots_dir,
                f"{item.name}_{status}.png"
            )

            driver.save_screenshot(screenshot_path)

            print(f"\nScreenshot saved at: {screenshot_path}")


def pytest_unconfigure(config):

    print("\n------- TESTS COMPLETE -------")
    print("Generating report...\n")

    allure_results_path = "reports/allure-results"
    html_report_path = "reports/report.html"

    if shutil.which("allure"):

        print("Opening Allure Report...")

        subprocess.Popen(
            ["allure", "serve", allure_results_path]
        )

    else:

        print("Allure command not found.")
        print("Opening HTML Report instead...")

        if os.path.exists(html_report_path):
            subprocess.Popen(
                ["open", html_report_path]
            )
        else:
            print("HTML report not found.")