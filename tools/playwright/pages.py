import allure
from playwright.sync_api import Playwright, Page

from config import settings, Browser


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,  # Добавляем параметр для типа браузера
        storage_state: str | None = None
) -> Page:
    """
    Инициализирует страницу Playwright с настройками из конфигурации
    
    Args:
        playwright: Экземпляр Playwright
        test_name: Имя теста для именования файлов
        browser_type: Тип браузера (Browser enum)
        storage_state: Путь к файлу состояния браузера
        
    Yields:
        Page: Инициализированная страница Playwright
    """
    # Динамически получаем нужный браузер
    browser = playwright[browser_type].launch(headless=settings.headless)
    
    context = browser.new_context(
        base_url=settings.get_base_url(),  # Используем base_url из настроек
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    # Сохраняем trace файл
    trace_path = settings.tracing_dir.joinpath(f'{test_name}.zip')
    context.tracing.stop(path=trace_path)
    
    browser.close()

    # Прикрепляем файлы к Allure отчету
    allure.attach.file(trace_path, name='trace', extension='zip')
    if page.video and page.video.path():
        allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)