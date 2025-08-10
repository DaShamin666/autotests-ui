import pytest
from playwright.sync_api import Page

# Предполагается наличие pages.login_page.LoginPage в проекте; если нет, можно позже добавить
try:
    from pages.login_page import LoginPage  # type: ignore
except Exception:  # pragma: no cover
    LoginPage = None  # type: ignore

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.fixture
def login_page(chromium_page: Page):  # type: ignore
    if LoginPage is None:
        pytest.skip("LoginPage is not implemented in this project")
    return LoginPage(page=chromium_page)  # type: ignore


@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)


@pytest.fixture
def courses_list_page(chromium_page: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page)


@pytest.fixture
def create_course_page(chromium_page: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page)


@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page_with_state)


@pytest.fixture
def courses_list_page_with_state(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)