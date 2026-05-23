import os
import subprocess


if __name__ == "__main__":

    os.makedirs("reports/allure-results", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    print("Running BDD Tests...\n")

    behave_command = (
        "behave "
        "-f allure_behave.formatter:AllureFormatter "
        "-o reports/allure-results "
        "features"
    )

    subprocess.run(
        behave_command,
        shell=True
    )

    print("\nBDD Execution Completed")
    print("Opening Allure Report...\n")

    allure_command = (
        "npx allure-commandline serve "
        "reports/allure-results"
    )

    subprocess.run(
        allure_command,
        shell=True
    )