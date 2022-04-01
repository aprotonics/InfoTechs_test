from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(RegistrationPage, self).__init__(*args, **kwargs)

    def check_url(self):
        current_url = self.driver.current_url

        assert 'client-registration' in current_url, f'"client-registration" not in {current_url}'

    def register(self):
        register_button = self.driver.find_element(*RegistrationPageLocators.register_button_selector)
        register_button.click()

        success_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.success_title_selector)
        )

        self.success_title_value = success_title.text

        client_id = self.driver.find_element(*RegistrationPageLocators.client_id_selector).text
        client_secret = self.driver.find_element(*RegistrationPageLocators.client_secret_selector).text
        user_login = self.driver.find_element(*RegistrationPageLocators.user_login_selector).text
        user_password = self.driver.find_element(*RegistrationPageLocators.user_password_selector).text
        self.credentials = {
            'client_id': client_id,
            'client_secret': client_secret,
            'user_login': user_login,
            'user_password': user_password}

    def check_registration(self):
        assert 'Great' in self.success_title_value, f'Great not in {self.success_title_value}'
        
        self.driver.get(self.url)

        div_register = self.driver.find_element(*RegistrationPageLocators.div_register_selector)
        div_register_class_name = div_register.get_attribute('class')
        div_register_is_hidden = 'hidden' in div_register_class_name

        div_already_registered = self.driver.find_element(*RegistrationPageLocators.div_already_registered_selector)
        div_already_registered_class_name = div_already_registered.get_attribute('class')
        div_already_registered_is_hidden = 'hidden' in div_already_registered_class_name

        assert div_register_is_hidden, f'div_register is not hidden'
        assert not div_already_registered_is_hidden, f'div_already_registered is hidden'
    
    def reset_registration(self):
        self.driver.get(self.url)
        
        view_register_button = self.driver.find_element(*RegistrationPageLocators.view_register_button_selector)
        view_register_button.click()

        reset_session_button = self.driver.find_element(*RegistrationPageLocators.reset_session_button_selector)
        reset_session_button.click()

    def check_reset_registration(self):
        div_register = self.driver.find_element(*RegistrationPageLocators.div_register_selector)
        div_register_class_name = div_register.get_attribute('class')
        div_register_is_hidden = 'hidden' in div_register_class_name

        div_already_registered = self.driver.find_element(*RegistrationPageLocators.div_already_registered_selector)
        div_already_registered_class_name = div_already_registered.get_attribute('class')
        div_already_registered_is_hidden = 'hidden' in div_already_registered_class_name

        assert not div_register_is_hidden, f'div_register is hidden'
        assert div_already_registered_is_hidden, f'div_already_registered is not hidden'
    