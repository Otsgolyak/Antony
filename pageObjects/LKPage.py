# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from pageObjects.BasePage import BasePage
# from selenium.webdriver.common.by import By
# from pageObjects.logger import *
#
#
# class LKPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     def button_trade(self):
#         return self.element(By.CSS_SELECTOR, "#bs-navbar-collapse-1 > form > "
#                                              "button.btn.btn-default.navbar-btn.btn-margin")
#
#     def profile_button(self):
#         return self.element(By.CSS_SELECTOR, "#root > div > div > div.main > div > ul > li.active > a")
#
#     def exit_menu(self):
#         return self.element(By.CSS_SELECTOR, "#bs-navbar-collapse-1 > form > a.exit-menu > svg")
#
#     def is_lk_window_loaded(self):
#         try:
#             logger.info("Checking LK")
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
#                 (By.CSS_SELECTOR, "#bs-navbar-collapse-1 > form > button.btn.btn-default.navbar-btn.btn-margin")))
#             logger.info("LK OK")
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
#                 (By.CSS_SELECTOR, "#root > div > div > div.main > div > ul > li.active > a")))
#             logger.info("LK OK")
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
#                 (By.CSS_SELECTOR, "#bs-navbar-collapse-1 > form > a.exit-menu > svg")))
#             logger.info("LK OK")
#         except NoSuchElementException:
#             logger.info("Failed")
