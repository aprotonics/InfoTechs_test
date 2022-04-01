import time
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from .locators import AuthWithDeviceCodePageLocators


class AuthWithDeviceCodePage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(AuthWithDeviceCodePage, self).__init__(*args, **kwargs)

    def request_device_code(self):
        start_button = self.driver.find_element(*AuthWithDeviceCodePageLocators.start_button_selector)
        start_button.click()

        time.sleep(1.5)

    def tell_to_enter_code(self):
        response_with_code = self.driver.find_element(*AuthWithDeviceCodePageLocators.response_with_code_selector).text

        self.device_code = response_with_code.split('\n')[1].split('"')[0]
        self.user_code = response_with_code.split('\n')[2].split('"')[0]

        print(self.device_code)
        print(self.user_code)

        continue_button = self.driver.find_element(*AuthWithDeviceCodePageLocators.continue_button_selector)
        actions = ActionChains(self.driver)
        actions.move_to_element(continue_button).click(continue_button).perform()

        time.sleep(1.5)
   
    def poll_token_endpoint(self):
        poll_button = self.driver.find_element(*AuthWithDeviceCodePageLocators.poll_button_selector)
        actions = ActionChains(self.driver)
        actions.move_to_element(poll_button).click(poll_button).perform()

        is_request_appeared = False
        while not is_request_appeared:
            is_request_appeared = self.is_request_appeared()

    def is_request_appeared(self):
        div_poll_pending = self.driver.find_element(*AuthWithDeviceCodePageLocators.div_poll_pending_selector)
        div_poll_pending_class_name = div_poll_pending.get_attribute('class')
        div_poll_pending_is_hidden = 'hidden' in div_poll_pending_class_name

        div_poll_success = self.driver.find_element(*AuthWithDeviceCodePageLocators.div_poll_success_selector)
        div_poll_success_class_name = div_poll_success.get_attribute('class')
        div_poll_success_is_hidden = 'hidden' in div_poll_success_class_name

        if not div_poll_pending_is_hidden and div_poll_success_is_hidden:
            poll_again_button = self.driver.find_element(*AuthWithDeviceCodePageLocators.poll_again_button_selector)
            poll_again_button.click()

            return False
        else: 
            return True      

    def check_access_token_appeared(self):
        token_response = self.driver.find_element(*AuthWithDeviceCodePageLocators.token_response_selector).text
        self.access_token = token_response.split('\n')[4].split('"')[3]

        assert 'access_token' in token_response, f'"access_token" not in {token_response}'
        assert self.access_token in token_response, f'{self.access_token} not in {token_response}'
        assert len(self.access_token) > 0, f'len of {self.access_token} = 0'
