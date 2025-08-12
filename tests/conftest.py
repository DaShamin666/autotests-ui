import pytest
from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest

# импорт фикстур страниц
from fixtures.pages import *  # noqa: F401,F403
from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from tools.routes import AppRoute
from config import settings


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    """
    Фикстура для регистрации пользователя и сохранения состояния браузера.
    Выполняется один раз за всю сессию тестирования.
    Использует первый браузер из списка settings.browsers.
    """
    # Используем первый браузер из списка для инициализации состояния
    first_browser = settings.browsers[0]
    browser = playwright[first_browser].launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())  # Добавили base_url
    page = context.new_page()

    # Работаем с регистрационной страницей через Page Object
    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)  # Используем AppRoute
    registration_page.registration_form.fill(
        email=settings.test_user.email,      # Используем settings
        username=settings.test_user.username, # Используем settings
        password=settings.test_user.password  # Используем settings
    )
    registration_page.click_registration_button()

    # Сохранение состояния браузера
    context.storage_state(path=settings.browser_state_file)  # Используем settings
    
    browser.close()


@pytest.fixture(params=settings.browsers)  # Добавляем параметризацию
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    """Новый Page для каждого теста с tracing и video на всех браузерах."""
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,  # Передаем браузер как параметр
        storage_state=None
    )


@pytest.fixture(params=settings.browsers)  # Добавляем параметризацию
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    """
    Фикстура для создания страницы браузера с сохраненным состоянием на всех браузерах.
    Использует сохраненное состояние из файла browser-state.json.
    """
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,  # Передаем браузер как параметр
        storage_state=settings.browser_state_file  # Используем settings
    )

