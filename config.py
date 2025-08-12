# config.py
import os
from enum import Enum
from typing import Self

from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    app_url: HttpUrl = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course"
    headless: bool = True  # По умолчанию True для CI/CD, можно переопределить в .env
    browsers: list[Browser] = [Browser.CHROMIUM, Browser.WEBKIT]  # По умолчанию только chromium и webkit
    test_user: TestUser = TestUser(
        email="user.name@gmail.com",
        username="username", 
        password="password"
    )
    test_data: TestData = TestData(
        image_png_file="./testdata/files/image.png"
    )
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath  # Добавили новое поле
    browser_state_file: FilePath

    def get_base_url(self) -> str:
        """Возвращает базовый URL для Playwright"""
        return f"{self.app_url}/"

    @classmethod
    def initialize(cls) -> Self:
        """Инициализирует настройки и создает необходимые директории и файлы"""
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        allure_results_dir = DirectoryPath("./allure-results")  # Создаем объект пути к папке
        browser_state_file = FilePath("browser-state.json")

        # Создаем директории, если они не существуют
        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)  # Создаем папку allure-results, если она не существует
        # Создаем файл состояния браузера, если его нет
        browser_state_file.touch(exist_ok=True)

        # Возвращаем модель с инициализированными значениями
        return cls(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,  # Передаем allure_results_dir в инициализацию настроек
            browser_state_file=browser_state_file
        )


# Инициализируем настройки глобально
settings = Settings.initialize()