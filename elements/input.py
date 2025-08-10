from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Input(BaseElement):
    def get_locator(self, **kwargs) -> Locator:
        """Переопределяем для работы с input тегами внутри элемента."""
        return super().get_locator(**kwargs).locator('input')

    def fill(self, value: str, **kwargs):
        """Заполняет поле ввода указанным текстом."""
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs):
        """Проверяет значение, находящееся в поле ввода."""
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)