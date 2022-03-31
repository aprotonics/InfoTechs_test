from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs) -> None:
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_reg_page(self):
        link = self.driver.find_element(*MainPageLocators.link_selector)
        link.click()
    