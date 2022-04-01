from selenium.webdriver.common.by import By


# Locators
class MainPageLocators():
    link_selector = (By.CSS_SELECTOR, 'p.no-client > a')

class RegistrationPageLocators():
    register_button_selector = (By.CSS_SELECTOR, 'a.register-new')
    success_title_selector = (By.XPATH, '//*[@id="client-registration-modal"]//div[contains(@class, "success")]/h3[contains(text(),"Great")]')
    client_id_selector = (By.CSS_SELECTOR, '#client-registration-modal table .client-id')
    client_secret_selector = (By.CSS_SELECTOR, '#client-registration-modal table .client-secret')
    user_login_selector = (By.CSS_SELECTOR, '#client-registration-modal table .user-login')
    user_password_selector = (By.CSS_SELECTOR, '#client-registration-modal table .user-password')
    div_register_selector = (By.CSS_SELECTOR, 'div.hide-when-registered')
    div_already_registered_selector = (By.CSS_SELECTOR, 'div.already-registered')
    view_register_button_selector = (By.CSS_SELECTOR, 'a.view-registration')
    reset_session_button_selector = (By.CSS_SELECTOR, '#client-registration-modal a.reset-session')

class LoginPageLocators():
    username_input_selector = (By.CSS_SELECTOR, 'input#username')
    password_input_selector = (By.CSS_SELECTOR, 'input#password')
    submit_button_selector = (By.CSS_SELECTOR, 'a#log-in-button')
    approve_button_selector = (By.CSS_SELECTOR, 'a#redirect-uri')

class AuthWithCodePageLocators():
    state_parameter_selector = (By.CSS_SELECTOR, '.auth-url-string .oauth2-state')
    auth_button_selector = (By.CSS_SELECTOR, 'a.auth-url')
    continue_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="2"]')
    go_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="3"]')
    success_message_selector = (By.XPATH, '//p[contains(@class, "success-message")][contains(text(),"Great")]')
    token_response_selector = (By.CSS_SELECTOR, '.token-response')

class AuthWithCodeAndPkceLocators():
    generate_code_verifier_button_selector = (By.CSS_SELECTOR, 'a.generate-code-verifier')
    code_verifier_selector = (By.CSS_SELECTOR, '.code-verifier')
    generate_code_challenge_button_selector = (By.CSS_SELECTOR, 'a.generate-code-challenge')
    code_challenge_selector = (By.CSS_SELECTOR, '.code-challenge')
    continue_button_selector1 = (By.CSS_SELECTOR, '.card-footer a[data-step="1"]')
    state_parameter_selector = (By.CSS_SELECTOR, '.auth-url-string .oauth2-state')
    auth_button_selector = (By.CSS_SELECTOR, 'a.auth-url')
    continue_button_selector2 = (By.CSS_SELECTOR, '.card-footer a[data-step="3"]')
    go_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="4"]')
    success_message_selector = (By.XPATH, '//p[contains(@class, "success-message")][contains(text(),"Great")]')
    token_response_selector = (By.CSS_SELECTOR, '.token-response')

class AuthWithDeviceCodePageLocators():
    start_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="1"]')
    response_with_code_selector = (By.CSS_SELECTOR, '#step-2 .content pre')
    continue_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="2"]')
    poll_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="3"]')
    div_poll_pending_selector = (By.CSS_SELECTOR, '#poll-pending')
    div_poll_success_selector = (By.CSS_SELECTOR, '#poll-success')
    poll_again_button_selector = (By.CSS_SELECTOR, '.card-footer a[data-step="3"]')
    token_response_selector = (By.CSS_SELECTOR, '#poll-success pre')
