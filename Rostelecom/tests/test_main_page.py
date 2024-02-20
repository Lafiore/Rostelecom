import re
import pytest
from playwright.sync_api import expect
from pages.page_objects.main_page import MainPage

expect.set_options(timeout=10_000)

#Позитивные тесты

def test_signup_form(main_page: MainPage) -> None: #Проверяем, что форма регистрации работает
    main_page.load()
    main_page.locators.SIGNUP_BUTTON.click()
    main_page.fill_signup_form()
    main_page.locators.SIGNUP_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration.+'))


@pytest.mark.parametrize('tab_name,user_login',
                         [('MOBILE', '89531196062'), ('EMAIL', 'kraevatv@yandex.ru'),
                          ('LOGIN', 'admin'), ('PERSONAL_ACCOUNT', '741852963573')])
def test_signin(main_page: MainPage, tab_name, user_login) -> None: #Проверяем, что авторизация возможна всеми способами
    main_page.load()
    main_page.fill_signin_form(tab_name, user_login)
    main_page.locators.SIGNIN_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://b2c.passport.rt.ru/account_b2c/page.+'))


@pytest.mark.parametrize('tabs,login',
                         [('MOBILE', '89531196062'), ('EMAIL', 'kraevatv@yandex.ru'),
                          ('LOGIN', 'admin'), ('PERSONAL_ACCOUNT', '741852963573')])
def test_recovery_form(main_page: MainPage, tabs, login) -> None: #Проверяем, что восстановление пароля возможно всеми способами
    main_page.load()
    main_page.locators.FORGOT_PASSWORD.click()
    main_page.fill_recovery_form(tabs,login)
    main_page.locators.CONTINUE_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate.+'))

def test_help_window(main_page: MainPage) -> None: #Проверяем, что модальное окно помощи открывается
    main_page.load()
    main_page.locators.HELP_WINDOW_LINK.click()
    expect(main_page.locators.HELP_WINDOW).to_be_visible()

def test_vk_auth_possible(main_page: MainPage) -> None:  #Проверяем, что авторизация через ВКонтате возможна
    main_page.load()
    main_page.locators.VK_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://id.vk.com/auth?return_auth_hash=10fe256621a69e3ed4&redirect_uri=https%3A%2F%2Fb2c.passport.rt.ru%2Fsocial%2Fadapter%2Fvk%2Fauth&redirect_uri_hash=6c0f16c920ab698a88&force_hash=&app_id=6771961.+'))

def test_ok_auth_possible(main_page: MainPage) -> None: #Проверяем, что авторизация через Одноклассники воможна
    main_page.load()
    main_page.locators.OK_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://connect.ok.ru/dk?st.cmd=OAuth2Login&st.redirect=%252Fdk%253Fst.cmd.+'))

def test_mail_auth_possible(main_page: MainPage) -> None: #Проверяем, что авторизация через Мэйл возможна
    main_page.load()
    main_page.locators.MAIL_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://connect.mail.ru/oauth/authorize?scope=login%3Aemail&state=pCSVM0cP_2uALA7n5SoJ-Jtld8BQhdXc-TgUqwR3490.YrenNxWEHqw.account_b2c&response_type=code&client_id=762573.+'))

def test_yandex_auth_possible(main_page: MainPage) -> None: #Проверяем, что авторизация через Яндекс возможна
    main_page.load()
    main_page.locators.YANDEX_BUTTON.click()
    expect(main_page.page).to_have_url(re.compile(r'https://oauth.yandex.ru/authorize?scope=login%3Aemail&state=mZPPQ6v553lDyBNittT_J47G0xMSlLk252q3unPvsPs.69J5odOFJGk.account_b2c&response_type=code&client_id=cca955e781554be08e4007813ddd578e.+'))

#Негативные тесты

def test_fill_incorrect_password(main_page: MainPage) -> None: #Проверяем, что при вводе некорректного пароля авторизация невозможна
    main_page.load()
    main_page.locators.USERNAME_FIELD.type('89531196062')
    main_page.locators.PASSWORD_FIELD.type('ttt12345')
    main_page.locators.SIGNIN_BUTTON.click()
    expect(main_page.locators.INCORRECT_LOGPASS).to_be_visible()

def test_no_letter_in_mobile(main_page: MainPage) -> None: #Проверяем, что в поле для ввода номера телефона нельзя ввести буквы
    main_page.load()
    main_page.locators.MOBILE.click()
    main_page.locators.USERNAME_FIELD.type('aaaaa')
    expect(main_page.locators.USERNAME_FIELD).is_empty()
    #Обнаружен баг. Смотрите баг-репорт №1

def test_number_needs_11_sign(main_page: MainPage) -> None: #Проверяем, что номер телефона должен содержать 11 цифр
    main_page.load()
    main_page.locators.MOBILE.click()
    main_page.locators.USERNAME_FIELD.type('895311960')
    main_page.locators.SIGNIN_BUTTON.click()
    expect(main_page.locators.MOBILE_WARNING).to_be_visible()

def test_fill_incorrect_email(main_page: MainPage) -> None: #Проверяем, что авторизация с некорретным e-mail невозможна
    main_page.load()
    main_page.locators.EMAIL.click()
    main_page.locators.USERNAME_FIELD.type('kraevatv@yandex.ru')
    main_page.locators.PASSWORD_FIELD.type('Tatyana123')
    main_page.locators.SIGNIN_BUTTON.click()
    expect(main_page.locators.INCORRECT_LOGPASS).to_be_visible()

def test_fill_incorrect_login(main_page: MainPage) -> None: #Проверяем, что авторизация с некорретным логином невозможна
    main_page.load()
    main_page.locators.LOGIN.click()
    main_page.locators.USERNAME_FIELD.type('admin111')
    main_page.locators.PASSWORD_FIELD.type('Tatyana123')
    main_page.locators.SIGNIN_BUTTON.click()
    expect(main_page.locators.INCORRECT_LOGPASS).to_be_visible()

def test_personal_account_needs_12_sign(main_page: MainPage) -> None: #Проверяем, что лицевой счет должен иметь 12 цифр
    main_page.load()
    main_page.locators.PERSONAL_ACCOUNT.click()
    main_page.locators.USERNAME_FIELD.type('74185296357')
    main_page.locators.PASSWORD_FIELD.type('Tatyana123')
    main_page.locators.SIGNIN_BUTTON.click()
    expect(main_page.locators.PERSONAL_ACCOUNT_WARNING).to_be_visible()