import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import AuthWithCodeAndPkceLocators


class AuthWithCodeAndPkcePage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(AuthWithCodeAndPkcePage, self).__init__(*args, **kwargs)

    def create_code_verifier_and_challenge(self):
        generate_code_verifier_button = self.driver.find_element(*AuthWithCodeAndPkceLocators.generate_code_verifier_button_selector)
        generate_code_verifier_button.click()
        self.code_verifier = self.driver.find_element(*AuthWithCodeAndPkceLocators.code_verifier_selector).text

        generate_code_challenge_button = self.driver.find_element(*AuthWithCodeAndPkceLocators.generate_code_challenge_button_selector)
        generate_code_challenge_button.click()
        self.code_challenge = self.driver.find_element(*AuthWithCodeAndPkceLocators.code_challenge_selector).text

        continue_button = self.driver.find_element(*AuthWithCodeAndPkceLocators.continue_button_selector1)
        continue_button.click()

        time.sleep(1.5)

    def build_auth_url(self):
        self.state_parameter = self.driver.find_element(*AuthWithCodeAndPkceLocators.state_parameter_selector).text
        auth_button = self.driver.find_element(*AuthWithCodeAndPkceLocators.auth_button_selector)
        actions = ActionChains(self.driver)
        actions.move_to_element(auth_button).click(auth_button).perform()

    def verify_state_parameter(self):
        current_url = self.driver.current_url
        state_parameter_in_url = current_url.split('?')[1].split('&')[0].split('=')[1]

        assert state_parameter_in_url == self.state_parameter, f'{state_parameter_in_url} !== {self.state_parameter}'

        continue_button = self.driver.find_element(*AuthWithCodeAndPkceLocators.continue_button_selector2)
        continue_button.click()

        time.sleep(1.5)
    
    def exchange_auth_code(self):
        go_button = self.driver.find_element(*AuthWithCodeAndPkceLocators.go_button_selector)
        actions = ActionChains(self.driver)
        actions.move_to_element(go_button).click(go_button).perform()

    def check_access_token_appeared(self):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AuthWithCodeAndPkceLocators.success_message_selector)
        )

        token_response = self.driver.find_element(*AuthWithCodeAndPkceLocators.token_response_selector).text
        self.access_token = token_response.split('\n')[3].split('"')[3]

        print(self.access_token)

        assert 'access_token' in token_response, f'"access_token" not in {token_response}'
        assert self.access_token in token_response, f'{self.access_token} not in {token_response}'
        assert len(self.access_token) > 0, f'len of {self.access_token} = 0'
