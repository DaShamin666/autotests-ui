from playwright.sync_api import sync_playwright, Page, expect


def save_browser_state(context):
    context.storage_state(path='storage_state.json')


def load_browser_state(browser):
    return browser.new_context(storage_state='storage_state.json')


def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()

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

        save_browser_state(context)

        context.close()

        new_context = load_browser_state(browser)
        new_page = new_context.new_page()

        new_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        new_page.wait_for_timeout(2000)

        expect(new_page.locator('h6[data-testid="courses-list-toolbar-title-text"]')).to_have_text("Courses")