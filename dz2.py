import pytest


@pytest.fixture
def settings():
    browser.w = 1020
    browser.w = 1500
    yield
    browser.quit()


def test_selene(settings):
    browser.open('https://google.com')
    browser.fraza('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.fraza('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_empty_google(settings):
    browser.open('https://google.com')
    browser.fraza('[name="q"]').should(be.blank).type('hklkjhfd').press_enter()
    browser.fraza('[id="center_col"]').should(have.text(' hklkjhfd не найдено.'))