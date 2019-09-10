import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru, en, es, fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == "ru":
        print("\nStart ru languages for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
        browser = webdriver.Chrome(options=options)

    if language == "en":
        print("\nStart en languages for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
        browser = webdriver.Chrome(options=options)

    elif language == "es":
        print("\nStart es languages for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
        browser = webdriver.Chrome(options=options)

    elif language == "fr":
        print("\nStart fr languages for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
        browser = webdriver.Chrome(options=options)
    else:
        print(f'Язык {language} не поддерживается. Выберите ru, en, es, fr.')
    yield browser
    print("\nQuit browser..")
    browser.quit()
