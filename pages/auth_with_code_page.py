import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import AuthWithCodePageLocators


class AuthWithCodePage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(AuthWithCodePage, self).__init__(*args, **kwargs)

    def build_auth_url(self):
        self.state_parameter = self.driver.find_element(*AuthWithCodePageLocators.state_parameter_selector).text
        auth_button = self.driver.find_element(*AuthWithCodePageLocators.auth_button_selector)
        auth_button.click()

    def verify_state_parameter(self):
        current_url = self.driver.current_url
        state_parameter_in_url = current_url.split('?')[1].split('&')[0].split('=')[1]

        assert state_parameter_in_url == self.state_parameter, f'{state_parameter_in_url} !== {self.state_parameter}'

        continue_button = self.driver.find_element(*AuthWithCodePageLocators.continue_button_selector)
        continue_button.click()

        time.sleep(1.5)

    def exchange_auth_code(self):
        go_button = self.driver.find_element(*AuthWithCodePageLocators.go_button_selector)
        actions = ActionChains(self.driver)
        actions.move_to_element(go_button).click(go_button).perform()
    
    def check_access_token_appeared(self):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AuthWithCodePageLocators.success_message_selector)
        )

        token_response = self.driver.find_element(*AuthWithCodePageLocators.token_response_selector).text
        self.access_token = token_response.split('\n')[3].split('"')[3]

        print(self.access_token)

        assert 'access_token' in token_response, f'"access_token" not in {token_response}'
        assert self.access_token in token_response, f'{self.access_token} not in {token_response}'
        assert len(self.access_token) > 0, f'len of {self.access_token} = 0'
