import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password"),
    ],
    ids=[
        "invalid_email_and_password",
        "invalid_email_empty_password",
        "empty_email_invalid_password"
    ]
)
def test_wrong_email_or_password_authorization(email: str, password: str, chromium_page):
    """
    Проверяем, что пользователь не может войти в систему с невалидными email и password.
    """
    page = chromium_page

    # Переход на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Заполнение полей
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(email)

    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(password)

    # Нажатие кнопки входа
    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    # Проверка, что пользователь не попал на дашборд
    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).not_to_be_visible()

    # Проверка, что остались на странице логина
    assert "login" in page.url or "auth" in page.url