from selenium.webdriver.common.by import By


# Locators
class MainPageLocators():
    link_selector = (By.CSS_SELECTOR, 'p.no-client > a')
    pass

class RegistrationPageLocators():
    pass

class LoginPageLocators():
    username_input_selector = (By.CSS_SELECTOR, 'input#username')
    password_input_selector = (By.CSS_SELECTOR, 'input#password')
    submit_button_selector = (By.CSS_SELECTOR, 'a#log-in-button')
    approve_button_selector = (By.CSS_SELECTOR, 'a#redirect-uri')
    pass

class AuthWithCodePageLocators():
    pass

class AuthWithCodeAndPkceLocators():
    pass



# registrations_fixture
register_button_selector = (By.CSS_SELECTOR, 'a.register-new')
success_title_selector = (By.XPATH, '//*[@id="client-registration-modal"]//div[contains(@class, "success")]/h3[contains(text(),"Great")]')
client_id_selector = (By.CSS_SELECTOR, '#client-registration-modal table .client-id')
client_secret_selector = (By.CSS_SELECTOR, '#client-registration-modal table .client-secret')
user_login_selector = (By.CSS_SELECTOR, '#client-registration-modal table .user-login')
user_password_selector = (By.CSS_SELECTOR, '#client-registration-modal table .user-password')

# test_transition_to_reg_page
link_selector = (By.CSS_SELECTOR, 'p.no-client > a')

# test_registration
div_register_selector = (By.CSS_SELECTOR, 'div.hide-when-registered')
div_already_registered_selector = (By.CSS_SELECTOR, 'div.already-registered')

# test_reset_registration
view_register_button_selector = (By.CSS_SELECTOR, 'a.view-registration')
reset_session_button_selector = (By.CSS_SELECTOR, '#client-registration-modal a.reset-session')
div_register_selector = (By.CSS_SELECTOR, 'div.hide-when-registered')
div_already_registered_selector = (By.CSS_SELECTOR, 'div.already-registered')

# test_auth_with_auth_code
state_parameter_selector = (By.CSS_SELECTOR, '.auth-url-string .oauth2-state')
auth_button_selector = (By.CSS_SELECTOR, 'a.auth-url')
username_input_selector = (By.CSS_SELECTOR, 'input#username')
password_input_selector = (By.CSS_SELECTOR, 'input#password')
submit_button_selector = (By.CSS_SELECTOR, 'a#log-in-button')
approve_button_selector = (By.CSS_SELECTOR, 'a#redirect-uri')
continue_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="2"]')
go_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="3"]')
success_message_selector = (By.XPATH, '//p[contains(@class, "success-message")][contains(text(),"Great")]')
token_response_selector = (By.CSS_SELECTOR, '.token-response')

# test_auth_with_auth_code_and_pkce
generate_code_verifier_button_selector = (By.CSS_SELECTOR, 'a.generate-code-verifier')
code_verifier_selector = (By.CSS_SELECTOR, '.code-verifier')
generate_code_challenge_button_selector = (By.CSS_SELECTOR, 'a.generate-code-challenge')
code_challenge_selector = (By.CSS_SELECTOR, '.code-challenge')
continue_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="1"]')
state_parameter_selector = (By.CSS_SELECTOR, '.auth-url-string .oauth2-state')
auth_button_selector = (By.CSS_SELECTOR, 'a.auth-url')
username_input_selector = (By.CSS_SELECTOR, 'input#username')
password_input_selector = (By.CSS_SELECTOR, 'input#password')
submit_button_selector = (By.CSS_SELECTOR, 'a#log-in-button')
approve_button_selector = (By.CSS_SELECTOR, 'a#redirect-uri')
continue_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="3"]')
go_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="4"]')
success_message_selector = (By.XPATH, '//p[contains(@class, "success-message")][contains(text(),"Great")]')
token_response_selector = (By.CSS_SELECTOR, '.token-response')
