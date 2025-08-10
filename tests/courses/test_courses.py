import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page_with_state: CoursesListPage):
        """
        Тест для проверки пустого списка курсов.
        Использует фикстуру courses_list_page_with_state для работы с авторизованной сессией.
        """
        # Переход на страницу курсов
        courses_list_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        
        # Проверка компонентов навигации
        courses_list_page_with_state.navbar.check_visible("username")
        courses_list_page_with_state.sidebar.check_visible()
        
        # Проверка заголовка страницы курсов и кнопки создания курса
        courses_list_page_with_state.toolbar_view.check_visible()
        
        # Проверка пустого блока
        courses_list_page_with_state.check_visible_empty_view()

    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        """
        Тест для проверки создания курса.
        Использует фикстуры create_course_page и courses_list_page.
        """
        # 1. Открыть страницу создания курса
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        
        # 2. Проверить наличие заголовка "Create course"
        create_course_page.check_visible_create_course_title()
        
        # 3. Проверить, что кнопка создания курса недоступна для нажатия
        create_course_page.check_disabled_create_course_button()
        
        # 4-5. Проверить, что блок загрузки изображения отображается без картинки (включая пустой блок)
        create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
        
        # 6. Проверить, что форма создания курса отображается с дефолтными значениями
        create_course_page.check_visible_create_course_form(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )
        
        # 7-8. Проверить наличие заголовка "Exercises" и кнопки создания задания
        create_course_page.check_visible_exercises_title()
        
        # 9. Убедиться, что отображается блок с пустыми заданиями
        create_course_page.check_visible_exercises_empty_view()
        
        # 10. Загрузить изображение для превью курса
        create_course_page.upload_preview_image("./testdata/files/image.png")
        
        # 11. Убедиться, что блок загрузки изображения показывает загруженную картинку
        create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
        
        # 12. Заполнить форму создания курса
        create_course_page.fill_create_course_form(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        
        # 13. Нажать на кнопку создания курса
        create_course_page.click_create_course_button()
        
        # 14-15. Проверить наличие заголовка "Courses" и кнопки создания курса (редирект на страницу со списком курсов)
        courses_list_page.toolbar_view.check_visible()
        
        # 16. Проверить корректность отображаемых данных на карточке курса
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        """
        Тест для проверки редактирования курса.
        E2E тест: создание курса → редактирование → проверка изменений.
        """
        # 1. Открыть страницу создания курса
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        
        # 2. Заполнить форму создания курса валидными данными и загрузить изображение
        create_course_page.upload_preview_image("./testdata/files/image.png")
        create_course_page.fill_create_course_form(
            title="Original Course",
            estimated_time="1 week",
            description="Original Description",
            max_score="50",
            min_score="5"
        )
        
        # 3. Нажать на кнопку создания курса
        create_course_page.click_create_course_button()
        
        # 4. Проверить, что на странице courses отображается карточка созданного курса
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Original Course",
            max_score="50",
            min_score="5",
            estimated_time="1 week"
        )
        
        # 5. Через меню карточки курса нажать на кнопку "Edit"
        courses_list_page.click_edit_course(index=0)
        
        # 6. Изменить поля курса на новые значения
        create_course_page.fill_create_course_form(
            title="Updated Course",
            estimated_time="3 weeks",
            description="Updated Description",
            max_score="200",
            min_score="20"
        )
        
        # 7. Нажать на кнопку сохранения изменений
        create_course_page.click_create_course_button()
        
        # 8. Проверить, что на странице courses отображается карточка курса с обновленными данными
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Updated Course",
            max_score="200",
            min_score="20",
            estimated_time="3 weeks"
        )