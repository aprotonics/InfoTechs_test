from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(LoginPage, self).__init__(*args, **kwargs)

    def login(self):
        pass

    def approve_access(self):
        pass
