from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    visibility_of_all_elements_located, alert_is_present, element_to_be_clickable, invisibility_of_element_located
from framework.utils.driver_utils import WebDriver
from framework.utils.config_manager import ConfigManager
from framework.utils.logger_utils import LoggerUtils


class WaitUtils:
    @staticmethod
    def wait_until_elem_is_visible(locator):
        WebDriverWait(WebDriver(), timeout=ConfigManager.get_config_data()["wait_time"]).\
            until(visibility_of_element_located(locator))

    @staticmethod
    def wait_until_elem_is_invisible(locator):
        WebDriverWait(WebDriver(), timeout=ConfigManager.get_config_data()["wait_time"]).\
            until(invisibility_of_element_located(locator))

    @staticmethod
    def wait_until_all_elems_are_visible():
        LoggerUtils().debug("Waiting until all elements are visible on the page")
        WebDriverWait(WebDriver(), timeout=ConfigManager.get_config_data()["wait_time"]).\
            until(visibility_of_all_elements_located)

    @staticmethod
    def wait_until_alert_is_present():
        LoggerUtils().debug("Waiting until an alert appears on the page")
        return WebDriverWait(WebDriver(), timeout=ConfigManager.get_config_data()["wait_time"]).\
            until(alert_is_present())

    @staticmethod
    def wait_until_elem_is_clickable(elem):
        WebDriverWait(WebDriver(), timeout=ConfigManager.get_config_data()["wait_time"]).\
            until(element_to_be_clickable(elem))

    @staticmethod
    def wait_until_elem_is_visible_checking_more_often(locator):
        WebDriverWait(
            WebDriver(),
            timeout=ConfigManager.get_config_data()["wait_time"],
            poll_frequency=ConfigManager.get_config_data()["poll_frequency"]).\
                until(visibility_of_element_located(locator))
