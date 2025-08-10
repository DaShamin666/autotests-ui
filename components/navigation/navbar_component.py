from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar_logo = Image(page, 'navbar-logo', 'Navbar logo')
        self.navbar_username = Text(page, 'navbar-username-text', 'Username')
        self.navbar_avatar = Image(page, 'navbar-avatar', 'User avatar')

    def check_visible(self, username: str):
        """Проверяет видимость компонента навбара и отображение имени пользователя"""
        self.navbar_logo.check_visible()
        self.navbar_avatar.check_visible()
        
        self.navbar_username.check_visible()
        self.navbar_username.check_have_text(username)