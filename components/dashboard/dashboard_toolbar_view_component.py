import allure  # Импортируем allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Dashboard title')

    @allure.step("Check visible dashboard toolbar")  # Добавили allure шаг
    def check_visible(self):
        """Проверяет корректность отображения панели управления"""
        self.title.check_visible()
        self.title.check_have_text('Dashboard')