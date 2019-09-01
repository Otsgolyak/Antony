from pageObjects.logger import *
from pageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TradePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def button_close(self):
        return self.element(By.CSS_SELECTOR, "#DepositModal > div > div > div.modal-header > button")

    def carret_wallet(self):
        return self.element(By.CSS_SELECTOR, "#PanelMenuHeader_account-group > span")

    def choose_wallet(self):
        return self.element(By.XPATH,
                            "//*[@id='app']/div/div[1]/div/div[2]/div[1]/div/div/div/div/div[4]/"
                            "div[2]/li/ul/div/div[1]/li[6]/a/div/span[2]")

    def caret_currency(self):
        return self.element(By.CSS_SELECTOR, "a#TradeView_list-ticker-group span")

    def currency_xpath(self):
        return self.element(By.XPATH, "//a[text()='BTC/USD']")

    def order_size(self):
        return self.element(By.CSS_SELECTOR, "input#orderSize")

    def confirmation_button(self):
        return self.element(By.CSS_SELECTOR, "div.MessageBox__buttons > button")

    def open_order(self):
        return self.element(By.CSS_SELECTOR, "div.TradeViewTickerButton__button.TradeViewTickerButton__button__buy")

    def positions_button(self):
        return self.element(By.CSS_SELECTOR, "div.react-grid-item.TradePage__content__info > div > "
                                             "div > ul > li:nth-child(2)")

    def check_position(self):
        return self.element(By.CSS_SELECTOR, "#PositionsTableBody > div > div.CustomScrollBars__view > div > div > "
                                             "div > div > div > div.app-table-cell.PositionsTable__cell-ticker > span")

    def close_position(self):
        return self.element(By.CSS_SELECTOR, "#PositionsTableBody > div > div.CustomScrollBars__view > div > div > "
                                             "div > div > div > "
                                             "div.app-table-cell.PositionsTable__cell-close.buttom-flex > button")

    def close_position_confirmation(self):
        return self.element(By.CSS_SELECTOR, "#InformationTabs__content > div > div > "
                                             "div.MessageBox.MessageBox-desktop-theme > div > div > "
                                             "div.MessageBox__buttons > button")

    def header_button(self):
        return self.element(By.CSS_SELECTOR, "div.HeaderButtons__setting > span")

    def log_out_button(self):
        return self.element(By.CSS_SELECTOR, "li:nth-child(21) > span")

    def is_trade_window_loaded(self):
        try:
            logger.info("Checking LK")
            self.ec_element(By.CSS_SELECTOR, "a#TradeView_list-ticker-group span")
            logger.info("LK OK")
            self.ec_element(By.CSS_SELECTOR, "div.TradeViewTickerButton__button.TradeViewTickerButton__button__buy")
            logger.info("LK OK")
            self.ec_element(By.CSS_SELECTOR, "li:nth-child(21) > span")
            logger.info("LK OK")
        except NoSuchElementException:
            logger.info("Failed")

    def if_position(self, text):
        try:
            assert self.check_position().text == text
            logger.info("Позиция открыта")
        except NoSuchElementException:
            logger.info("Позиции нет")
