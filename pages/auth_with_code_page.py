from .base_page import BasePage
from .locators import AuthWithCodePageLocators


class AuthWithCodePage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(AuthWithCodePage, self).__init__(*args, **kwargs)

    def build_auth_url(self):
        pass

    def verify_state_parameter(self):
        pass

    def exchange_auth_code(self):
        pass
    
    def check_access_token_appeared(self):
        pass
