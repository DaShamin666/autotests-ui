from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar_logo = page.get_by_test_id('navbar-logo')
        self.navbar_username = page.get_by_test_id('navbar-username-text')
        self.navbar_avatar = page.get_by_test_id('navbar-avatar')

    def check_visible(self, username: str):
        """Проверяет видимость компонента навбара и отображение имени пользователя"""
        expect(self.navbar_logo).to_be_visible()
        expect(self.navbar_avatar).to_be_visible()
        
        expect(self.navbar_username).to_be_visible()
        expect(self.navbar_username).to_have_text(username)