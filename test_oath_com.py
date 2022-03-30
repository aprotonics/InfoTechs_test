import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


BASE_URL = 'https://www.oauth.com'
URL = 'https://www.oauth.com/playground/index.html'


@pytest.fixture(scope='function')
def registration(driver):
    URL = f'{BASE_URL}/playground/client-registration.html'

    driver.get(URL)

    register_button = driver.find_element(By.CSS_SELECTOR, 'a.register-new')
    register_button.click()

    success_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="client-registration-modal"]//div[contains(@class, "success")]/h3[contains(text(),"Great")]'))
    )

    success_title_value = success_title.text

    client_id = driver.find_element(By.CSS_SELECTOR, '#client-registration-modal table .client-id').text
    client_secret = driver.find_element(By.CSS_SELECTOR, '#client-registration-modal table .client-secret').text
    user_login = driver.find_element(By.CSS_SELECTOR, '#client-registration-modal table .user-login').text
    user_password = driver.find_element(By.CSS_SELECTOR, '#client-registration-modal table .user-password').text
    credentials = {
        'client_id': client_id,
        'client_secret': client_secret,
        'user_login': user_login,
        'user_password': user_password}

    registration = [driver, credentials, success_title_value]

    return registration


class Test():
    def test_transition_to_reg_page(self, driver):
        URL = f'{BASE_URL}/playground/index.html'

        self.driver = driver

        self.driver.get(URL)

        link = self.driver.find_element(By.CSS_SELECTOR, 'p.no-client > a')
        link.click()

        current_url = self.driver.current_url

        assert 'client-registration' in current_url, f'"client-registration" not in {current_url}'

    def test_registration(self, registration):
        URL = f'{BASE_URL}/playground/client-registration.html'

        self.driver, _, success_title_value = registration

        assert 'Great' in success_title_value, f'Great not in {success_title_value}'

        self.driver.get(URL)

        div_register = self.driver.find_element(By.CSS_SELECTOR, 'div.hide-when-registered')
        div_register_class_name = div_register.get_attribute('class')
        div_register_is_hidden = 'hidden' in div_register_class_name

        div_already_registered = self.driver.find_element(By.CSS_SELECTOR, 'div.already-registered')
        div_already_registered_class_name = div_already_registered.get_attribute('class')
        div_already_registered_is_hidden = 'hidden' in div_already_registered_class_name

        assert div_register_is_hidden, f'div_register is not hidden'
        assert not div_already_registered_is_hidden, f'div_already_registered is hidden'

    def test_reset_registration(self, registration):
        URL = f'{BASE_URL}/playground/client-registration.html'

        self.driver, *_ = registration

        self.driver.get(URL)

        # Reset registration
        view_register_button = self.driver.find_element(By.CSS_SELECTOR, 'a.view-registration')
        view_register_button.click()

        reset_session_button = self.driver.find_element(By.CSS_SELECTOR, '#client-registration-modal a.reset-session')
        reset_session_button.click()

        # Check reset
        div_register = self.driver.find_element(By.CSS_SELECTOR, 'div.hide-when-registered')
        div_register_class_name = div_register.get_attribute('class')
        div_register_is_hidden = 'hidden' in div_register_class_name

        div_already_registered = self.driver.find_element(By.CSS_SELECTOR, 'div.already-registered')
        div_already_registered_class_name = div_already_registered.get_attribute('class')
        div_already_registered_is_hidden = 'hidden' in div_already_registered_class_name

        assert not div_register_is_hidden, f'div_register is hidden'
        assert div_already_registered_is_hidden, f'div_already_registered is not hidden'

    def test_auth_with_auth_code(self, registration):
        URL = f'{BASE_URL}/playground/authorization-code.html'

        self.driver, credentials, *_ = registration

        self.driver.get(URL)

        # Build the Authorization URL
        state_parameter = self.driver.find_element(By.CSS_SELECTOR, '.auth-url-string .oauth2-state').text
        auth_button = self.driver.find_element(By.CSS_SELECTOR, 'a.auth-url')
        auth_button.click()

        # Log In
        username_input = self.driver.find_element(By.CSS_SELECTOR, 'input#username')
        username_input.send_keys(credentials['user_login'])
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input#password')
        password_input.send_keys(credentials['user_password'])
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'a#log-in-button')
        submit_button.click()

        approve_button = self.driver.find_element(By.CSS_SELECTOR, 'a#redirect-uri')
        approve_button.click()

        # Verify the state parameter
        current_url = self.driver.current_url
        state_parameter_in_url = current_url.split('?')[1].split('&')[0].split('=')[1]

        assert state_parameter_in_url == state_parameter, f'{state_parameter_in_url} !== {state_parameter}'

        continue_button = self.driver.find_element(By.CSS_SELECTOR, '.card-footer a[data-step="2"]')
        continue_button.click()

        time.sleep(1.5)

        # Exchange the Authorization Code
        go_button = self.driver.find_element(By.CSS_SELECTOR, '.card-footer a[data-step="3"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(go_button).click(go_button).perform()

        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//p[contains(@class, "success-message")][contains(text(),"Great")]'))
        )

        token_response = self.driver.find_element(By.CSS_SELECTOR, '.token-response').text
        access_token = token_response.split('\n')[3].split('"')[3]

        print(access_token)

        assert 'access_token' in token_response, f'"access_token" not in {token_response}'
        assert len(access_token) > 0, f'len of {access_token} = 0'

    def test_auth_with_auth_code_and_pkce(self, registration):
        URL = f'{BASE_URL}/playground/authorization-code-with-pkce.html'

        self.driver, credentials, *_ = registration

        self.driver.get(URL)

        # Create a Code Verifier and Challenge
        generate_code_verifier_button = self.driver.find_element(By.CSS_SELECTOR, 'a.generate-code-verifier')
        generate_code_verifier_button.click()
        code_verifier = self.driver.find_element(By.CSS_SELECTOR, '.code-verifier').text

        generate_code_challenge_button = self.driver.find_element(By.CSS_SELECTOR, 'a.generate-code-challenge')
        generate_code_challenge_button.click()
        code_challenge = self.driver.find_element(By.CSS_SELECTOR, '.code-challenge').text

        continue_button = self.driver.find_element(By.CSS_SELECTOR, '.card-footer a[data-step="1"]')
        continue_button.click()

        time.sleep(1.5)

        # Build the Authorization URL
        state_parameter = self.driver.find_element(By.CSS_SELECTOR, '.auth-url-string .oauth2-state').text
        auth_button = self.driver.find_element(By.CSS_SELECTOR, 'a.auth-url')
        actions = ActionChains(self.driver)
        actions.move_to_element(auth_button).click(auth_button).perform()

        # Log In
        username_input = self.driver.find_element(By.CSS_SELECTOR, 'input#username')
        username_input.send_keys(credentials['user_login'])
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input#password')
        password_input.send_keys(credentials['user_password'])
        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'a#log-in-button')
        submit_button.click()

        approve_button = self.driver.find_element(By.CSS_SELECTOR, 'a#redirect-uri')
        approve_button.click()

        time.sleep(0.5)

        # Verify the state parameter
        current_url = self.driver.current_url
        state_parameter_in_url = current_url.split('?')[1].split('&')[0].split('=')[1]

        assert state_parameter_in_url == state_parameter, f'{state_parameter_in_url} !== {state_parameter}'

        continue_button = self.driver.find_element(By.CSS_SELECTOR, '.card-footer a[data-step="3"]')
        continue_button.click()
        
        time.sleep(1.5)

        # Exchange the Authorization Code
        go_button = self.driver.find_element(By.CSS_SELECTOR, '.card-footer a[data-step="4"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(go_button).click(go_button).perform()

        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//p[contains(@class, "success-message")][contains(text(),"Great")]'))
        )

        token_response = self.driver.find_element(By.CSS_SELECTOR, '.token-response').text
        access_token = token_response.split('\n')[3].split('"')[3]

        print(access_token)

        assert 'access_token' in token_response, f'"access_token" not in {token_response}'
        assert len(access_token) > 0, f'len of {access_token} = 0'
