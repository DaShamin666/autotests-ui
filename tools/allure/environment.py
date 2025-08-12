"""
Модуль для создания файла environment.properties для Allure отчетов.
Этот файл содержит информацию об окружении тестирования.
"""

import sys
from pathlib import Path

# Добавляем корневую директорию проекта в sys.path
sys.path.append(str(Path(__file__).parent.parent.parent))

from config import settings


def create_allure_environment_file():
    """
    Создает файл environment.properties в директории allure-results
    с информацией об окружении тестирования.
    
    Файл будет содержать все настройки из config.py в формате:
    key=value
    """
    # Получаем настройки в виде словаря
    settings_dict = settings.model_dump()
    
    # Создаем отформатированные строки для каждого параметра
    items = []
    for key, value in settings_dict.items():
        # Форматируем значения для лучшей читаемости
        if isinstance(value, dict):
            # Для вложенных словарей (test_user, test_data) выводим их поля
            formatted_dict = {k: str(v) for k, v in value.items()}
            formatted_value = str(formatted_dict)
        elif isinstance(value, list):
            # Для списков браузеров выводим их названия
            if key == 'browsers':
                formatted_value = '[' + ', '.join([browser.value for browser in value]) + ']'
            else:
                formatted_value = str(value)
        else:
            formatted_value = str(value)
        
        items.append(f'{key}={formatted_value}')
    
    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на запись
    environment_file_path = settings.allure_results_dir.joinpath('environment.properties')
    
    with open(environment_file_path, 'w+', encoding='utf-8') as file:
        file.write(properties)  # Записываем переменные в файл
    
    print(f"✅ Файл environment.properties создан: {environment_file_path}")


if __name__ == "__main__":
    # Для тестирования функции
    create_allure_environment_file()