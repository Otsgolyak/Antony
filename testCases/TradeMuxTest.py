import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.TradePage import TradePage

from pageObjects.logger import *


class TradeMuxTest(unittest.TestCase):
    baseURL = "https://trade.trademux.net/#/auth"
    TradePageUrl = "https://trade.trademux.net/#/"
    LKURL = "https://trade.trademux.net/cabinet/clientarea/profile"
    username = "*"
    password = "*"
    order_size = "10.0"
    currency = "BTC/USD"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        logger.info("Test started")
        cls.driver.get(cls.baseURL)
        login_page = LoginPage(cls.driver)
        login_page.textbox_email().send_keys(cls.username)
        login_page.do_send_keys(cls.textbox_email(), cls.username)
        login_page.textbox_password().send_keys(cls.password)
        login_page.login_button().click()
        logger.info("Logging in")
        time.sleep(2)

    def test_trade(self):
        logger.info("Open TradePage")
        self.driver.get(self.TradePageUrl)
        trade_page = TradePage(self.driver)
        trade_page.button_close().click()
        logger.info("Setting wallet")
        trade_page.carret_wallet().click()
        trade_page.choose_wallet().click()
        logger.info("Wallet set")
        logger.info("Setting currency")
        trade_page.caret_currency().click()
        trade_page.currency_xpath().click()
        logger.info("Currency set")
        trade_page.order_size().clear()
        trade_page.order_size().send_keys(self.order_size)
        trade_page.order_size().send_keys(self.order_size)
        logger.info("Opening position")
        trade_page.open_order().click()
        trade_page.confirmation_button().click()
        logger.info("Position opened")
        logger.info("Closing position")
        trade_page.positions_button().click()
        trade_page.if_position(self.currency)
        trade_page.close_position().click()
        trade_page.close_position_confirmation().click()
        logger.info("Position closed")
        trade_page.header_button().click()
        trade_page.log_out_button().click()
        logger.info('Test finished')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
