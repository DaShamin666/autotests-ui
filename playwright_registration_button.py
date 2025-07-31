from playwright.sync_api import Page,expect


def test(page: Page):
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    button_element = page.locator('//button[@id="registration-page-registration-button"]')
    expect(button_element).to_be_disabled()

    email = page.locator('//input[@id=":r0:"]')
    expect(email).to_be_visible()
    email.fill("user.name@gmail.com")

    username = page.locator('//input[@id=":r1:"]')
    expect(username).to_be_visible()
    username.fill("username")

    password = page.locator('//input[@id=":r2:"]')
    expect(password).to_be_visible()
    password.fill("password")

    button_element2 = page.locator('//button[@id="registration-page-registration-button"]')
    expect(button_element2).to_be_visible()
