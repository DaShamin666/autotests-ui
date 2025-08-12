"""
Фикстуры для работы с Allure отчетами.
"""

import pytest

from tools.allure.environment import create_allure_environment_file


@pytest.fixture(scope='session', autouse=True)
def save_allure_environment_file():
    """
    Автоматически создает файл environment.properties после завершения всех тестов.
    
    Эта фикстура:
    - Запускается автоматически для каждой тестовой сессии (autouse=True)
    - Имеет область действия session (scope='session')
    - Выполняется после завершения всех тестов (yield)
    - Создает файл environment.properties с информацией об окружении
    """
    # До начала автотестов ничего не делаем
    yield  # Запускаются автотесты...
    
    # После завершения автотестов создаем файл environment.properties
    print("\n🔧 Создание файла environment.properties для Allure отчета...")
    create_allure_environment_file()