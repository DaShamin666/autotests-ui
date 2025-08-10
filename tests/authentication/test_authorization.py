import pytest

from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ],
        ids=[
            "invalid_email_and_password",
            "invalid_email_empty_password", 
            "empty_email_invalid_password"
        ]
    )
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        """
        E2E тест успешной авторизации:
        1. Регистрация нового пользователя
        2. Проверка Dashboard и выход из системы
        3. Авторизация с теми же данными
        4. Проверка повторного входа на Dashboard
        """
        # 1. Регистрация нового пользователя
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_button()

        # 2. Проверяем, что открылась страница Dashboard и нажимаем кнопку "Logout"
        dashboard_page.check_visible_dashboard_title()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        # 3. Заполняем форму авторизации и нажимаем кнопку "Login"
        login_page.login_form.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_button()

        # 4. Проверяем, что открылась страница Dashboard
        dashboard_page.check_visible_dashboard_title()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()

    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        """
        Тест навигации со страницы авторизации на страницу регистрации
        """
        # 1. Открываем страницу авторизации
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        
        # 2. Нажимаем на ссылку "Registration"
        login_page.click_registration_link()
        
        # 3. Проверим, что отображается форма регистрации
        registration_page.registration_form.check_visible(email="", username="", password="")