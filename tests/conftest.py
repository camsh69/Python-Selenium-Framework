import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    # True for headless, False to launch test in browser
    headless = False
    # choose browser to run test, default is chrome - 'pytest --browser_name=firefox' for example
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--start-maximised")
            # options.add_argument("--window-size=1920x1080")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


# pytest.hookimpl(hookwrapper=True)


# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])

# if report.when == "call" or report.when == "setup":
#     xfail = hasattr(report, "wasxfail")
#     if (report.skipped and xfail) or (report.failed and not xfail):
#         file_name = report.nodeid.replace("::", "_") + ".png"
#         _capture_screenshot(file_name)
#         if file_name:
#             html = (
#                 '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
#                 'onclick="window.open(this.src)" align="right"/></div>' % file_name
#             )
#             extra.append(pytest_html.extras.html(html))
#     report.extra = extra


# def _capture_screenshot(name):
#     driver.save_screenshot(name)
