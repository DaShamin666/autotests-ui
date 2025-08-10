import pytest
from playwright.sync_api import sync_playwright, Playwright, Page

# импорт фикстур страниц
from fixtures.pages import *  # noqa: F401,F403
from pages.authentication.registration_page import RegistrationPage


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

        # Работаем с регистрационной страницей через Page Object
        registration_page = RegistrationPage(page=page)
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
        registration_page.click_registration_button()

        # Сохранение состояния браузера
        context.storage_state(path="browser-state.json")
        
        browser.close()


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    """Новый Chromium Page для каждого теста."""
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    try:
        yield page
    finally:
        context.close()
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

