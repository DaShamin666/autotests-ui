import pytest
from dashboard_page import DashboardPage


@pytest.fixture
def dashboard_page(page):
    """Фикстура для инициализации страницы Dashboard."""
    return DashboardPage(page)
