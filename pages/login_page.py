import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, *args, credentials, **kwargs) -> None:
        super(LoginPage, self).__init__(*args, **kwargs)

        self.credentials = credentials

    def login(self):
        username_input = self.driver.find_element(*LoginPageLocators.username_input_selector)
        username_input.send_keys(self.credentials['user_login'])
        password_input = self.driver.find_element(*LoginPageLocators.password_input_selector)
        password_input.send_keys(self.credentials['user_password'])
        submit_button = self.driver.find_element(*LoginPageLocators.submit_button_selector)
        submit_button.click()

    def approve_access(self):
        approve_button = self.driver.find_element(*LoginPageLocators.approve_button_selector)
        approve_button.click()

        time.sleep(0.5)
