from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):

        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    # метод проверяющий наличие ссылки

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.login_link), "Login link isn't presented"
