from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage


class LoginPage(BasePage):

    def textbox_email(self):
        return self.element(By.CSS_SELECTOR, "#loginInput")

    def textbox_password(self):
        return self.element(By.CSS_SELECTOR, "#loginPassword")

    def login_button(self):
        return self.element(By.CSS_SELECTOR, "button:nth-child(2)")
