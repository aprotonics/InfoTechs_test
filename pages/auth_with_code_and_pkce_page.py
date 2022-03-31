from .base_page import BasePage
from .locators import AuthWithCodeAndPkceLocators


class AuthWithCodeAndPkcePage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(AuthWithCodeAndPkcePage, self).__init__(*args, **kwargs)

    def create_code_verifier_and_challenge(self):
        pass

    def build_auth_url(self):
        pass

    def verify_state_parameter(self):
        pass
    
    def exchange_auth_code(self):
        pass

    def check_access_token_appeared(self):
        pass
    