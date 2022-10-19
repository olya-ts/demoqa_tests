from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Button, ProgressBar
from framework.utils.config_manager import ConfigManager
from framework.utils.logger_utils import LoggerUtils


class ProgressBarPage(BaseForm):
    __start_button = Button(
        locator=(By.XPATH, "//button[text()='Start']"),
        elem_name="Start Button")

    __stop_button = Button(
        locator=(By.XPATH, "//button[text()='Stop']"),
        elem_name="Stop Button")

    __progress_bar = ProgressBar(
        locator=(By.XPATH, "//div[@role='progressbar']"),
        elem_name="Progress Bar")

    __progress_bar_with_age_value = ProgressBar(
        locator=(By.XPATH, f"//div[@role='progressbar'][@aria-valuenow='{ConfigManager.get_test_data()['age']}']"),
        elem_name="Progress Bar with the Age Value")

    def __init__(self):
        super().__init__(
            unique_element=self.__start_button,
            name="Progress Bar Page")

    def click_start_button(self):
        LoggerUtils().debug("Clicking Start Button on the '%s'", self._name)
        self.__start_button.click()

    def click_stop_button(self):
        LoggerUtils().debug("Clicking Stop Button on the '%s'", self._name)
        self.__stop_button.click()

    def get_progress_bar_value(self):
        LoggerUtils().debug("Getting value from Progress Bar attribute on the '%s'", self._name)
        return self.__progress_bar.get_attribute("aria-valuenow")

    def wait_until_progress_bar_with_age_value_appears_more_often(self):
        LoggerUtils().debug("Waiting more often until Progress Bar with the age value appears on the '%s'", self._name)
        self.__progress_bar_with_age_value.wait_until_elem_is_looked_for_more_often()
