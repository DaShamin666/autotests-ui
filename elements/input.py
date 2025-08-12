import allure  # Импортируем allure
from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("INPUT")


class Input(BaseElement):
    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "input"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """Переопределяем для работы с input тегами внутри элемента."""
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        """Заполняет поле ввода указанным текстом."""
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'
        
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        """Проверяет значение, находящееся в поле ввода."""
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'
        
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            expect(locator).to_have_value(value)