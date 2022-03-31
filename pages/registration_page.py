from .base_page import BasePage
from .locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(RegistrationPage, self).__init__(*args, **kwargs)

    def check_url(self):
        pass

    def register(self):
        pass

    def check_registration(self):
        pass
    
    def reset_registration(self):
        pass

    def check_reset_registration(self):
        pass
    