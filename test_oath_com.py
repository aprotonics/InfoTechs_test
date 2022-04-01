import pytest
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.auth_with_code_page import AuthWithCodePage
from pages.auth_with_code_and_pkce_page import AuthWithCodeAndPkcePage
from pages.auth_with_device_code_page import AuthWithDeviceCodePage


BASE_URL = 'https://www.oauth.com'


@pytest.fixture(scope='function')
def registration(driver):
    URL = f'{BASE_URL}/playground/client-registration.html'

    registration_page = RegistrationPage(driver, URL)
    registration_page.open()
    registration_page.register()

    return registration_page


class TestOathCom(): 

    def test_go_to_reg_page(self, driver):        
        URL = f'{BASE_URL}/playground/index.html'

        main_page = MainPage(driver, URL)
        main_page.open()
        main_page.go_to_reg_page()
        registration_page = RegistrationPage(main_page.driver, main_page.driver.current_url)
        registration_page.check_url()

    def test_registration(self, registration):
        URL = f'{BASE_URL}/playground/client-registration.html'

        registration_page = registration
        registration_page.check_registration()

    def test_reset_registration(self, registration):
        URL = f'{BASE_URL}/playground/client-registration.html'

        registration_page = registration
        registration_page.reset_registration()
        registration_page.check_reset_registration()

    def test_auth_with_auth_code(self, registration):
        URL = f'{BASE_URL}/playground/authorization-code.html'

        registration_page = registration
        auth_with_code_page = AuthWithCodePage(registration_page.driver, URL)
        auth_with_code_page.open()
        auth_with_code_page.build_auth_url()
        login_page = LoginPage(
            auth_with_code_page.driver,
            auth_with_code_page.driver.current_url,
            credentials=registration_page.credentials)
        login_page.login()
        login_page.approve_access()
        auth_with_code_page.verify_state_parameter()
        auth_with_code_page.exchange_auth_code()
        auth_with_code_page.check_access_token_appeared()

    def test_auth_with_auth_code_and_pkce(self, registration):
        URL = f'{BASE_URL}/playground/authorization-code-with-pkce.html'

        registration_page = registration
        auth_with_code_and_pkce_page = AuthWithCodeAndPkcePage(registration_page.driver, URL)
        auth_with_code_and_pkce_page.open()
        auth_with_code_and_pkce_page.create_code_verifier_and_challenge()
        auth_with_code_and_pkce_page.build_auth_url()
        login_page = LoginPage(
            auth_with_code_and_pkce_page.driver,
            auth_with_code_and_pkce_page.driver.current_url,
            credentials=registration_page.credentials)
        login_page.login()
        login_page.approve_access()
        auth_with_code_and_pkce_page.verify_state_parameter()
        auth_with_code_and_pkce_page.exchange_auth_code()
        auth_with_code_and_pkce_page.check_access_token_appeared()
    
    def test_auth_with_device_code(self, registration):
        URL = f'{BASE_URL}/playground/device-code.html'

        registration_page = registration
        auth_with_device_code_page = AuthWithDeviceCodePage(registration_page.driver, URL)
        auth_with_device_code_page.open()
        auth_with_device_code_page.request_device_code()
        auth_with_device_code_page.tell_to_enter_code()
        auth_with_device_code_page.poll_token_endpoint()
        auth_with_device_code_page.check_access_token_appeared()
