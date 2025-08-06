from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_registration_form_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_registration_form_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_registration_form_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_form_button = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form_email_input(self, email: str):
        self.email_registration_form_input.fill(email)

    def fill_registration_form_username_input(self, username: str):
        self.username_registration_form_input.fill(username)

    def fill_registration_form_password_input(self, password: str):
        self.password_registration_form_input.fill(password)

    def click_registration_form_button(self):
        self.registration_form_button.click()