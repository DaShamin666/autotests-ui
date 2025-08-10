from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    def check_enabled(self, **kwargs):
        """Проверяет, что кнопка доступна для взаимодействия."""
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_enabled()

    def check_disabled(self, **kwargs):
        """Проверяет, что кнопка недоступна для взаимодействия."""
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_disabled()