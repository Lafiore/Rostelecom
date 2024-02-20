from playwright.sync_api import Page


class MainPageLocators:
    def __init__(self, page: Page):
        self.SIGNUP_BUTTON = page.get_by_text("Зарегистрироваться").first
        self.NAME_FIELD = page.locator("input[name=\"firstName\"]")
        self.LASTNAME_FIELD = page.locator("input[name=\"lastName\"]")
        self.REGION_FIELD = page.locator("input[type=\"text\"]").nth(2)
        self.REGION_OPTION = page.get_by_text("Воронежская обл")
        self.MOBILE_NUMBER_FIELD = page.locator("#address")
        self.PASSWORD_FIELD = page.locator("#password")
        self.PASSWORD_CONFIRM_FIELD = page.locator("#password-confirm")

        self.USERNAME_FIELD = page.locator("#username")
        self.SIGNIN_BUTTON = page.get_by_role("button", name="Войти")

        self.MOBILE = page.get_by_text("Телефон", exact=True)
        self.EMAIL = page.get_by_text("Почта")
        self.LOGIN = page.get_by_text("Логин")
        self.PERSONAL_ACCOUNT = page.get_by_text("Лицевой счёт")

        self.FORGOT_PASSWORD = page.get_by_role("link", name="Забыл пароль")
        self.CONTINUE_BUTTON = page.get_by_role("button", name="Продолжить")
        self.INCORRECT_LOGPASS = page.get_by_text("Неверный логин или пароль")

        self.HELP_WINDOW_LINK = page.get_by_text("Помощь", exact=True)
        self.HELP_WINDOW = page.get_by_text("Ростелеком ID").nth(1)
        self.MOBILE_WARNING = page.get_by_text("Неверный формат телефона")
        self.PERSONAL_ACCOUNT_WARNING = page.get_by_text("Проверьте, пожалуйста, номер лицевого счета")

        self.VK_BUTTON = page.locator("#oidc_vk")
        self.OK_BUTTON = page.locator("#oidc_ok")
        self.MAIL_BUTTON = page.locator("#oidc_mail")
        self.YANDEX_BUTTON = page.locator("#oidc_ya")


