import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.auth_with_code_page import AuthWithCodePage
from pages.auth_with_code_and_pkce_page import AuthWithCodeAndPkcePage

from pages.locators import *


BASE_URL = 'https://www.oauth.com'
URL = 'https://www.oauth.com/playground/index.html'


@pytest.fixture(scope='function')
def registration(driver):
    URL = f'{BASE_URL}/playground/client-registration.html'

    registration_page = RegistrationPage(driver, URL)
    registration_page.open()
    registration_page.register()

    # driver.get(URL)

    # register_button = driver.find_element(*register_button_selector)
    # register_button.click()

    # success_title = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located(*success_title_selector)
    # )

    # success_title_value = success_title.text

    # client_id = driver.find_element(*client_id_selector).text
    # client_secret = driver.find_element(*client_secret_selector).text
    # user_login = driver.find_element(*user_login_selector).text
    # user_password = driver.find_element(*user_password_selector).text
    # credentials = {
    #     'client_id': client_id,
    #     'client_secret': client_secret,
    #     'user_login': user_login,
    #     'user_password': user_password}

    # registration = [driver, credentials, success_title_value]

    return registration_page


class TestOathCom():  
    def test_go_to_reg_page(self, driver):        
        URL = f'{BASE_URL}/playground/index.html'

        main_page = MainPage(driver, URL)
        main_page.open()
        main_page.go_to_reg_page()
        registration_page = RegistrationPage(driver, URL)
        registration_page.check_url()

        # self.driver = driver

        # self.driver.get(URL)    

        # link = self.driver.find_element(*link_selector)
        # link.click()

        # current_url = self.driver.current_url

        # assert 'client-registration' in current_url, f'"client-registration" not in {current_url}'
        pass

    def test_registration(self, registration):
        URL = f'{BASE_URL}/playground/client-registration.html'

        # self.driver, _, success_title_value = registration

        registration_page = registration
        registration_page.check_registration()
        
        # assert 'Great' in success_title_value, f'Great not in {success_title_value}'
        
        # self.driver.get(URL)

        # div_register = self.driver.find_element(*div_register_selector)
        # div_register_class_name = div_register.get_attribute('class')
        # div_register_is_hidden = 'hidden' in div_register_class_name

        # div_already_registered = self.driver.find_element(*div_already_registered_selector)
        # div_already_registered_class_name = div_already_registered.get_attribute('class')
        # div_already_registered_is_hidden = 'hidden' in div_already_registered_class_name

        # assert div_register_is_hidden, f'div_register is not hidden'
        # assert not div_already_registered_is_hidden, f'div_already_registered is hidden'
        pass

    def test_reset_registration(self, registration):
        URL = f'{BASE_URL}/playground/client-registration.html'

        # self.driver, *_ = registration

        registration_page = registration
        registration_page.reset_registration()
        registration_page.check_reset_registration()

        # self.driver.get(URL)

        # # Reset registration
        # view_register_button = self.driver.find_element(*view_register_button_selector)
        # view_register_button.click()

        # reset_session_button = self.driver.find_element(*reset_session_button_selector)
        # reset_session_button.click()

        # # Check reset
        # div_register = self.driver.find_element(*div_register_selector)
        # div_register_class_name = div_register.get_attribute('class')
        # div_register_is_hidden = 'hidden' in div_register_class_name

        # div_already_registered = self.driver.find_element(*div_already_registered_selector)
        # div_already_registered_class_name = div_already_registered.get_attribute('class')
        # div_already_registered_is_hidden = 'hidden' in div_already_registered_class_name

        # assert not div_register_is_hidden, f'div_register is hidden'
        # assert div_already_registered_is_hidden, f'div_already_registered is not hidden'
        pass

    def test_auth_with_auth_code(self, registration):
        URL = f'{BASE_URL}/playground/authorization-code.html'

        # self.driver, credentials, *_ = registration

        registration_page = registration
        auth_with_code_page = AuthWithCodePage()
        auth_with_code_page.open()
        auth_with_code_page.build_auth_url()
        login_page = LoginPage()
        login_page.open()
        login_page.login()
        login_page.approve_access()
        auth_with_code_page.verify_state_parameter()
        auth_with_code_page.exchange_auth_code()
        auth_with_code_page.check_access_token_appeared()


        # self.driver.get(URL)

        # # Build the Authorization URL
        # state_parameter = self.driver.find_element(*state_parameter_selector).text
        # auth_button = self.driver.find_element(*auth_button_selector)
        # auth_button.click()

        # # Log In
        # username_input = self.driver.find_element(*username_input_selector)
        # username_input.send_keys(credentials['user_login'])
        # password_input = self.driver.find_element(*password_input_selector)
        # password_input.send_keys(credentials['user_password'])
        # submit_button = self.driver.find_element(*submit_button_selector)
        # submit_button.click()

        # approve_button = self.driver.find_element(*approve_button_selector)
        # approve_button.click()

        # # Verify the state parameter
        # current_url = self.driver.current_url
        # state_parameter_in_url = current_url.split('?')[1].split('&')[0].split('=')[1]

        # assert state_parameter_in_url == state_parameter, f'{state_parameter_in_url} !== {state_parameter}'

        # continue_button = self.driver.find_element(*continue_button_selector)
        # continue_button.click()

        # time.sleep(1.5)

        # # Exchange the Authorization Code
        # go_button = self.driver.find_element(*go_button_selector)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(go_button).click(go_button).perform()

        # success_message = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(*success_message_selector)
        # )

        # token_response = self.driver.find_element(*token_response_selector).text
        # access_token = token_response.split('\n')[3].split('"')[3]

        # print(access_token)

        # assert 'access_token' in token_response, f'"access_token" not in {token_response}'
        # assert len(access_token) > 0, f'len of {access_token} = 0'
        pass

    def test_auth_with_auth_code_and_pkce(self, registration):
        URL = f'{BASE_URL}/playground/authorization-code-with-pkce.html'

        # self.driver, credentials, *_ = registration

        registration_page = registration
        auth_with_code_and_pkce_page = AuthWithCodeAndPkcePage()
        auth_with_code_and_pkce_page.open()
        auth_with_code_and_pkce_page.create_code_verifier_and_challenge()
        auth_with_code_and_pkce_page.build_auth_url()
        login_page = LoginPage()
        login_page.open()
        login_page.login()
        login_page.approve_access()
        auth_with_code_and_pkce_page.verify_state_parameter()
        auth_with_code_and_pkce_page.exchange_auth_code()
        auth_with_code_and_pkce_page.check_access_token_appeared()

        # self.driver.get(URL)

        # # Create a Code Verifier and Challenge
        # generate_code_verifier_button = self.driver.find_element(*generate_code_verifier_button_selector)
        # generate_code_verifier_button.click()
        # code_verifier = self.driver.find_element(*code_verifier_selector).text

        # generate_code_challenge_button = self.driver.find_element(*generate_code_challenge_button_selector)
        # generate_code_challenge_button.click()
        # code_challenge = self.driver.find_element(*code_challenge_selector).text

        # continue_button = self.driver.find_element(*continue_button_selector)
        # continue_button.click()

        # time.sleep(1.5)

        # # Build the Authorization URL
        # state_parameter = self.driver.find_element(*state_parameter_selector).text
        # auth_button = self.driver.find_element(*auth_button_selector)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(auth_button).click(auth_button).perform()

        # # Log In
        # username_input = self.driver.find_element(*username_input_selector)
        # username_input.send_keys(credentials['user_login'])
        # password_input = self.driver.find_element(*password_input_selector)
        # password_input.send_keys(credentials['user_password'])
        # submit_button = self.driver.find_element(*submit_button_selector)
        # submit_button.click()

        # approve_button = self.driver.find_element(*approve_button_selector)
        # approve_button.click()

        # time.sleep(0.5)

        # # Verify the state parameter
        # current_url = self.driver.current_url
        # state_parameter_in_url = current_url.split('?')[1].split('&')[0].split('=')[1]

        # assert state_parameter_in_url == state_parameter, f'{state_parameter_in_url} !== {state_parameter}'

        # continue_button = self.driver.find_element(*continue_button_selector)
        # continue_button.click()
        
        # time.sleep(1.5)

        # # Exchange the Authorization Code
        # go_button = self.driver.find_element(*go_button_selector)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(go_button).click(go_button).perform()

        # success_message = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(*success_message_selector)
        # )

        # token_response = self.driver.find_element(*token_response_selector).text
        # access_token = token_response.split('\n')[3].split('"')[3]

        # print(access_token)

        # assert 'access_token' in token_response, f'"access_token" not in {token_response}'
        # assert len(access_token) > 0, f'len of {access_token} = 0'
        pass
