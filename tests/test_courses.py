from playwright.sync_api import expect
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    """
    Тест для проверки пустого списка курсов.
    Использует фикстуру chromium_page_with_state для работы с авторизованной сессией.
    """
    page = chromium_page_with_state
    
    # Переход на страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка заголовка страницы курсов
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    # Проверка иконки пустого состояния
    empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    # Проверка заголовка пустого состояния
    empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title).to_be_visible()
    expect(empty_view_title).to_have_text('There is no results')

    # Проверка описания пустого состояния
    empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description).to_be_visible()
    expect(empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
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
    
    # 4. Убедиться, что отображается пустой блок для предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()
    
    # 5. Проверить, что блок загрузки изображения отображается без картинки
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    
    # 6. Проверить, что форма создания курса отображается с дефолтными значениями
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    
    # 7. Проверить наличие заголовка "Exercises"
    create_course_page.check_visible_exercises_title()
    
    # 8. Проверить наличие кнопки создания задания
    create_course_page.check_visible_create_exercise_button()
    
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
    
    # 14. Проверить наличие заголовка "Courses" (редирект на страницу со списком курсов)
    courses_list_page.check_visible_courses_title()
    
    # 15. Проверить наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()
    
    # 16. Проверить корректность отображаемых данных на карточке курса
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )