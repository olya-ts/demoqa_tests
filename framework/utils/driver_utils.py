from selenium.common.exceptions import NoAlertPresentException
from framework.utils.logger_utils import LoggerUtils
from framework.driver.web_driver import WebDriver


class DriverUtils:
    @staticmethod
    def navigate(url):
        LoggerUtils().debug("Navigating to the url %s", url)
        WebDriver().get(url)

    @staticmethod
    def maximize_window():
        LoggerUtils().debug("Maximizing the window")
        WebDriver().maximize_window()

    @staticmethod
    def switch_to_alert():
        LoggerUtils().debug("Switching to an alert")
        return WebDriver().switch_to.alert

    @staticmethod
    def check_if_alert_is_on_page():
        LoggerUtils().debug("Checking if the alert is on the page")
        try:
            if DriverUtils.switch_to_alert():
                return True
        except NoAlertPresentException:
            LoggerUtils().warning("An alert hasn't been found on the page")
            return False

    @staticmethod
    def get_tab_id():
        LoggerUtils().debug("Getting the window/tab handle's id")
        return WebDriver().current_window_handle

    @staticmethod
    def switch_to_initial_tab(initial_tab_id):
        LoggerUtils().debug("Switching to the initial window/tab")
        WebDriver().switch_to.window(initial_tab_id)

    @staticmethod
    def switch_to_new_tab(initial_tab_id):
        LoggerUtils().debug("Switching to a new window/tab")
        for window_handle in WebDriver().window_handles:
            if window_handle != initial_tab_id:
                WebDriver().switch_to.window(window_handle)
                break

    @staticmethod
    def close_tab():
        LoggerUtils().debug("Closing the current window/tab")
        WebDriver().close()

    @staticmethod
    def switch_to_frame(by, frame, name):
        LoggerUtils().debug("Switching to the frame %s", name)
        WebDriver().switch_to.frame(WebDriver().find_element(by=by, value=frame))

    @staticmethod
    def switch_back_from_frame():
        LoggerUtils().debug("Switching back to the default content from the frame")
        WebDriver().switch_to.default_content()

    @staticmethod
    def execute_click(elem):
        LoggerUtils().debug("Clicking on the elem by means of javascript")
        WebDriver().execute_script("arguments[0].click();", elem)
