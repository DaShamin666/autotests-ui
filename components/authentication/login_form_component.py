import allure  # Импортируем allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input
from tools.logger import get_logger

logger = get_logger("LOGIN_FORM")


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')

    @allure.step("Fill login form")  # Добавили allure шаг
    def fill(self, email: str, password: str):
        """Заполняет форму с полями электронной почты и пароля"""
        logger.info(f"Filling login form with email '{email}' and password")  # Добавили логирование
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    @allure.step("Check visible login form")  # Добавили allure шаг
    def check_visible(self, email: str, password: str):
        """Проверяет корректность отображения формы и введённых данных"""
        logger.info(f"Checking login form visibility with email '{email}' and password")  # Добавили логирование
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)