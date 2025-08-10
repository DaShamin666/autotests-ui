from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Input(BaseElement):
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """Переопределяем для работы с input тегами внутри элемента."""
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        """Заполняет поле ввода указанным текстом."""
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        """Проверяет значение, находящееся в поле ввода."""
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)