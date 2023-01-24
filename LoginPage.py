from selenium import webdriver
# from Web.Base.selenium_driver import SeleniumDriver
from Web.Base.SeleniumDriverMethods import SeleniumDriver
import time


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    login_email_textbox = "email"
    login_next_button = "//button[contains(text(),'Next')]"
    login_password_textbox = "password"
    user_name_home_page = "//span[contains(text(),'Demo User')]"

    def enter_login_email(self, username=""):
        self.send_key(username, self.login_email_textbox, "id")
        time.sleep(3)

    def enter_login_password(self, password=""):
        self.send_key(password, self.login_password_textbox, "id")
        time.sleep(3)

    def click_on_next_button(self):
        self.element_click(self.login_next_button, "xpath")
        time.sleep(3)

    def verify_home_page(self):
        status = self.is_element_present(self.user_name_home_page, "xpath")
        return status

