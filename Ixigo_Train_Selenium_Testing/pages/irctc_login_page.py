import time


class IRCTCLoginPage:

    def __init__(self, driver):

        self.driver = driver

    def skip_login(self):

        time.sleep(5)