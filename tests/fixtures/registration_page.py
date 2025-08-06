import pytest
from registration_page import RegistrationPage


@pytest.fixture
def registration_page(page):
    """Фикстура для инициализации страницы регистрации."""
    return RegistrationPage(page)
