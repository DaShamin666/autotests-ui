"""
Демонстрация использования логгера в автотестах.
Этот файл показывает правильные и неправильные способы использования логирования.
"""

from tools.logger import get_logger

# ✅ ПРАВИЛЬНО: Один логгер на файл, инициализация в начале
logger = get_logger("DEMO")


def good_logging_example():
    """Пример правильного использования логирования"""
    
    # ✅ ПРАВИЛЬНО: Логирование перед выполнением действия
    logger.info("Opening login page")
    # ... здесь был бы код открытия страницы
    
    logger.info("Filling email field")
    # ... здесь был бы код заполнения поля email
    
    logger.info("Clicking login button")
    # ... здесь был бы код клика по кнопке
    
    logger.info("Checking dashboard visibility")
    # ... здесь был бы код проверки дашборда


def bad_logging_example():
    """Пример неправильного использования логирования"""
    
    # ❌ ПЛОХО: Множественная инициализация логгеров
    logger1 = get_logger("DEMO")
    logger2 = get_logger("DEMO") 
    logger3 = get_logger("DEMO")
    
    # ❌ ПЛОХО: Логирование после выполнения действия
    # ... здесь был бы код открытия страницы
    logger1.info("Opened login page")  # Уже поздно логировать
    
    # ❌ ПЛОХО: Неинформативные сообщения
    logger2.info("Action completed")  # Какое действие?
    logger3.info("Test")  # Что тестируем?


def comprehensive_logging_example():
    """Пример комплексного логирования с разными уровнями"""
    
    logger.debug("Starting test execution")  # Отладочная информация
    logger.info("Opening application")       # Основные действия
    logger.warning("Using test credentials") # Предупреждения
    logger.error("Authentication failed")    # Ошибки
    logger.critical("System is unavailable") # Критические ошибки


if __name__ == "__main__":
    print("🟢 Правильный пример логирования:")
    good_logging_example()
    
    print("\n🔴 Неправильный пример логирования:")
    bad_logging_example()
    
    print("\n📊 Комплексный пример с разными уровнями:")
    comprehensive_logging_example()