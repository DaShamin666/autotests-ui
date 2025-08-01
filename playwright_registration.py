from playwright.sync_api import Page,expect


def test(page: Page):
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email = page.locator('//input[@id=":r0:"]')
    expect(email).to_be_visible()
    email.fill("user.name@gmail.com")

    username = page.locator('//input[@id=":r1:"]')
    expect(username).to_be_visible()
    username.fill("username")

    password = page.locator('//input[@id=":r2:"]')
    expect(password).to_be_visible()
    password.fill("password")

    button_element = page.locator('//button[@id="registration-page-registration-button"]')
    expect(button_element).to_be_visible()
    assert button_element.is_enabled(), "Кнопка должна быть доступна для клика"
    button_element.click()

    header_exists = page.locator('h6[data-testid="dashboard-toolbar-title-text"]').is_visible()

    if header_exists:
        print("Заголовок 'Dashboard' присутствует на странице.")
    else:
        print("Заголовок 'Dashboard' отсутствует на странице.")
