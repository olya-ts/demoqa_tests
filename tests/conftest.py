import pytest
from framework.utils.driver_utils import DriverUtils
from framework.driver.web_driver import WebDriver


@pytest.fixture
def maximize_window():
    DriverUtils.maximize_window()


@pytest.fixture
def quit_driver():
    yield
    WebDriver.quit_driver()
