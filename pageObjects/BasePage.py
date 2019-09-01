
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.logger import *


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def element(self, selector, locator):
        return self.wait.until(lambda driver: self.driver.find_element(selector, locator))

    def ec_element(self, selector, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self, selector, locator))

    def do_send_keys(self, elem, text):
        for symbol in text:
            self.wait.until(elem.send_keys(symbol))


