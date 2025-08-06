import pytest
from playwright.sync_api import sync_playwright, Playwright, Page
from registration_page import RegistrationPage
from dashboard_page import DashboardPage


@pytest.fixture(scope="session")
def initialize_browser_state():
    """
    Фикстура для регистрации пользователя и сохранения состояния браузера.
    Выполняется один раз за всю сессию тестирования.
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Регистрация пользователя
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохранение состояния браузера
        context.storage_state(path="browser-state.json")
        
        browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    """
    Фикстура для создания страницы браузера с сохраненным состоянием.
    Использует сохраненное состояние из файла browser-state.json.
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    
    yield page
    
    context.close()
    browser.close()


@pytest.fixture
def registration_page(page):
    return RegistrationPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

