import os
import time
import logging
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    os.makedirs("logs", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("reports/allure-results", exist_ok=True)

    logging.basicConfig(
        filename="logs/bdd_execution.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
        filemode="w"
    )

    logging.info("===== BDD TEST EXECUTION STARTED =====")


def before_scenario(context, scenario):
    logging.info(f"Starting Scenario: {scenario.name}")

    options = Options()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://www.ixigo.com")

    time.sleep(5)


def after_step(context, step):
    status = "PASSED" if step.status == "passed" else "FAILED"

    screenshot_name = step.name.replace(" ", "_").replace("/", "_")
    screenshot_path = f"reports/screenshots/{screenshot_name}_{status}.png"

    context.driver.save_screenshot(screenshot_path)

    logging.info(f"Step: {step.name} -> {status}")
    logging.info(f"Screenshot saved at: {screenshot_path}")

    # Attach screenshot to Allure
    with open(screenshot_path, "rb") as image_file:
        allure.attach(
            image_file.read(),
            name=f"{step.name}_{status}",
            attachment_type=allure.attachment_type.PNG
        )

    # Attach step log to Allure
    allure.attach(
        f"Step Name: {step.name}\nStatus: {status}",
        name=f"Log - {step.name}",
        attachment_type=allure.attachment_type.TEXT
    )


def after_scenario(context, scenario):
    logging.info(f"Scenario Completed: {scenario.name}")

    context.driver.quit()


def after_all(context):
    logging.info("===== BDD TEST EXECUTION COMPLETED =====")

    # Attach complete log file to Allure
    log_file_path = "logs/bdd_execution.log"

    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as log_file:
            allure.attach(
                log_file.read(),
                name="Complete BDD Execution Log",
                attachment_type=allure.attachment_type.TEXT
            )

    print("\nBDD Test Execution Completed\n")