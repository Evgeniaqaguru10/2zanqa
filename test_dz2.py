import pytest
from selene import browser, be, have


@pytest.fixture
def settings():
    browser.config.window_width = 1020
    browser.config.window_width = 1500
    yield
    browser.quit()


def test_selene(settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_empty_google(settings):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('hklkjhfd').press_enter()
    browser.element('[id="center_col"]').should(have.text(' hklkjhfd не найдено.'))