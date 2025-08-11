import allure  # Импортируем allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Create course title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create course')

    @allure.step("Check visible create course toolbar")  # Добавили allure шаг
    def check_visible(self, is_create_course_disabled: bool = True):
        """Проверяет корректность отображения панели управления"""
        self.title.check_visible()
        self.title.check_have_text('Create course')

        self.create_course_button.check_visible()

        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    @allure.step("Click create course button")  # Добавили allure шаг
    def click_create_course_button(self):
        """Нажимает на кнопку создания курса"""
        self.create_course_button.click()