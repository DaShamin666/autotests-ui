from enum import Enum


class AppRoute(str, Enum):
    """Маршруты приложения для автотестов"""
    LOGIN = "./#/auth/login"
    REGISTRATION = "./#/auth/registration"
    DASHBOARD = "./#/dashboard"
    COURSES = "./#/courses"
    COURSES_CREATE = "./#/courses/create"