# Ixigo Train Booking BDD Automation Framework

## Project Overview

This project is a BDD-based Selenium automation framework for Ixigo Train Booking. It uses Python, Behave, Selenium WebDriver, Page Object Model, Excel test data, screenshots, logs, and Allure reporting.

## Tech Stack

- Python
- Selenium WebDriver
- Behave BDD
- Gherkin
- Page Object Model
- OpenPyXL
- Allure Report

## Project Structure

```text
Ixigo_Train_BDD_project
├── config
│   └── config.properties
├── features
│   ├── environment.py
│   ├── end_to_end.feature
│   ├── test_cases.feature
│   └── steps
│       ├── end_to_end_steps.py
│       └── test_cases_steps.py
├── pages
├── utilities
├── testdata
│   └── test_data.xlsx
├── reports
│   ├── allure-results
│   └── screenshots
├── logs
├── behave.ini
├── requirements.txt
└── README.md