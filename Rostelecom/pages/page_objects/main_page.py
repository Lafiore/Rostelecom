from playwright.sync_api import Page
from pages.locators.main_page_locators import MainPageLocators
from pages.page_objects.base_page import BasePage


class MainPage(BasePage):
    URL = 'https://b2c.passport.rt.ru/auth'

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.locators = MainPageLocators(page)

    def fill_signup_form(self):
        self.locators.NAME_FIELD.type("Татьяна")
        self.locators.LASTNAME_FIELD.type("Краева")
        self.locators.REGION_FIELD.type("Воронеж")
        self.locators.REGION_OPTION.click()
        self.locators.MOBILE_NUMBER_FIELD.type("89531206062")
        self.locators.PASSWORD_FIELD.type("Tatyana123")
        self.locators.PASSWORD_CONFIRM_FIELD.type("Tatyana123")

    def fill_signin_form(self, tab_name, user_login):
        getattr(self.locators, tab_name).click()
        self.locators.USERNAME_FIELD.type(user_login)
        self.locators.PASSWORD_FIELD.type("Tatyana123")

    def fill_recovery_form(self, tabs, login):
        getattr(self.locators, tabs).click()
        self.locators.USERNAME_FIELD.type(login)


