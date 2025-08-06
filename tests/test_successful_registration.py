import pytest

@pytest.mark.regression
def test_successful_registration(registration_page, dashboard_page):
    registration_page.page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form_email_input("user.name@gmail.com")
    registration_page.fill_registration_form_username_input("username")
    registration_page.fill_registration_form_password_input("password")
    registration_page.click_registration_form_button()
    dashboard_page.expect_dashboard_toolbar_title_text_visible()