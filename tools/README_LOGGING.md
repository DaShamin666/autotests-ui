# 📋 Система логирования в автотестах

## 🎯 Назначение

Система логирования обеспечивает детальное отслеживание выполнения автотестов на всех уровнях:
- **Страницы** (открытие, перезагрузка, проверка URL)
- **Компоненты** (заполнение форм, проверка видимости)
- **Элементы** (клики, ввод текста, проверки)

## 🔧 Использование

### Базовое использование

```python
from tools.logger import get_logger

# Инициализация логгера (один раз в начале файла)
logger = get_logger("COMPONENT_NAME")

# Логирование действий
logger.info("Filling login form")
logger.warning("Using default credentials")
logger.error("Login failed")
```

### Интеграция с Allure

```python
import allure
from tools.logger import get_logger

logger = get_logger("LOGIN_PAGE")

def login(self, email: str, password: str):
    step = f'Logging in with email "{email}"'
    with allure.step(step):
        logger.info(step)  # Логирование дублирует Allure шаг
        # ... выполнение действий
```

## 📊 Уровни логирования

| Уровень   | Назначение                    | Пример использования          |
|-----------|-------------------------------|-------------------------------|
| `DEBUG`   | Отладочная информация         | Внутренние операции          |
| `INFO`    | Основные действия            | Клики, заполнение полей      |
| `WARNING` | Предупреждения               | Использование тестовых данных |
| `ERROR`   | Ошибки                       | Неуспешные проверки          |
| `CRITICAL`| Критические ошибки           | Системные сбои               |

## 🏷️ Именование логгеров

Используйте понятные имена логгеров, отражающие их назначение:

- `BASE_ELEMENT` - базовые операции с элементами
- `INPUT` - работа с полями ввода
- `BUTTON` - работа с кнопками
- `LOGIN_FORM` - компонент формы входа
- `BASE_PAGE` - базовые операции со страницами

## ✅ Лучшие практики

### ✅ Правильно:

```python
# Один логгер на файл
logger = get_logger("SEARCH_PAGE")

def search(self, query: str):
    logger.info(f"Searching for '{query}'")  # Логирование ПЕРЕД действием
    self.search_input.fill(query)
    self.search_button.click()
```

### ❌ Неправильно:

```python
# Множественная инициализация
logger1 = get_logger("SEARCH")
logger2 = get_logger("SEARCH")  # Дублирование!

def search(self, query: str):
    self.search_input.fill(query)
    logger1.info("Search completed")  # Логирование ПОСЛЕ действия
```

## 📈 Пример вывода

```
2025-08-12 16:00:34,881 | BASE_PAGE | INFO | Opening the url "AppRoute.LOGIN"
2025-08-12 16:00:36,529 | LOGIN_FORM | INFO | Filling login form with email 'user@test.com' and password
2025-08-12 16:00:36,530 | BASE_ELEMENT | INFO | Getting locator with "data-testid=login-form-email-input" at index "0"
2025-08-12 16:00:36,530 | INPUT | INFO | Fill input "Email" to value "user@test.com"
2025-08-12 16:00:36,621 | BASE_ELEMENT | INFO | Clicking button "Login"
```

## 🎛️ Конфигурация

Логгер автоматически настраивается на:
- **Уровень**: DEBUG (показывает все сообщения)
- **Формат**: `время | имя_логгера | уровень | сообщение`
- **Вывод**: консоль (StreamHandler)

## 🔍 Отладка

Для детального анализа выполнения тестов используйте флаг `-s`:

```bash
python3 -m pytest tests/test_example.py -v -s
```

Это покажет все логи в реальном времени во время выполнения тестов.