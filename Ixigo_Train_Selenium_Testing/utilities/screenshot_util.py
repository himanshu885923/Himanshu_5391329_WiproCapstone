import time

def take_screenshot(driver, name):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(path)
    return path
