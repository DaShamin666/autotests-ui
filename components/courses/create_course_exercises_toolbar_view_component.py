import allure  # Импортируем allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Exercises title')
        self.create_exercise_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Create exercise')

    @allure.step("Check visible create course exercises toolbar")  # Добавили allure шаг
    def check_visible(self):
        """Проверяет корректность отображения панели управления"""
        self.title.check_visible()
        self.title.check_have_text('Exercises')

        self.create_exercise_button.check_visible()

    @allure.step("Click create exercise button")  # Добавили allure шаг
    def click_create_exercise_button(self):
        """Нажимает на кнопку создания задания"""
        self.create_exercise_button.click()