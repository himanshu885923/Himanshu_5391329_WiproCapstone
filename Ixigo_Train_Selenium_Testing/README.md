# Ixigo Train Booking Automation (Selenium + Python)

This project automates Ixigo → IRCTC train booking flow using:
- Selenium WebDriver (Chrome 147 macOS ARM64)
- Page Object Model (POM)
- PyTest

## To Run:
1. Install requirements:
   pip install -r requirements.txt

2. Place correct ChromeDriver in /drivers/
   Name it: chromedriver_147_mac_arm64

3. Run automation:
   pytest -v tests/test_end_to_end.py
