import allure
from playwright.sync_api import expect
from ui_coverage_tool import ActionType

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("BUTTON")


class Button(BaseElement):
    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        """Проверяет, что кнопка доступна для взаимодействия."""
        step = f'Checking that {self.type_of} "{self.name}" is enabled'
        
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

        # Трекаем проверку доступности как ENABLED
        self.track_coverage(ActionType.ENABLED, nth, **kwargs)

    def check_disabled(self, nth: int = 0, **kwargs):
        """Проверяет, что кнопка недоступна для взаимодействия."""
        step = f'Checking that {self.type_of} "{self.name}" is disabled'
        
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()

        # Трекаем проверку недоступности как DISABLED
        self.track_coverage(ActionType.DISABLED, nth, **kwargs)