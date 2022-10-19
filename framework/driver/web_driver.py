from framework.utils.logger_utils import LoggerUtils
from framework.driver.browser_factory import BrowserFactory


class WebDriver:
    _instance = None

    def __new__(cls, *args, **kwargs):
        LoggerUtils().debug("Checking if the driver exists and returning a new one if not")
        if not cls._instance:
            cls._instance = BrowserFactory.get_driver()
        return cls._instance

    @classmethod
    def quit_driver(cls):
        LoggerUtils().debug("Quiting the driver")
        cls._instance.quit()
        cls._instance = None
