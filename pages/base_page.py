import math

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import time

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #cause https://bugs.launchpad.net/ubuntu/+source/python-selenium/+bug/1833448
        #self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)
        time.sleep(5)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

