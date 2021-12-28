import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome" or "Chrome":
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox" or "Firefox":
        pass
    elif browser_name == "edge" or "Edge":
        pass

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
