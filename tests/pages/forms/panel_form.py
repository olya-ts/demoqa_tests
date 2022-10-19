from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Button
from framework.utils.logger_utils import LoggerUtils


class PanelForm(BaseForm):
    __alerts_button = Button(
        locator=(By.XPATH, "//span[text()='Alerts']"),
        elem_name="Alerts Button")

    __nested_frames_button = Button(
        locator=(By.XPATH, "//span[text()='Nested Frames']"),
        elem_name="Nested Frames Button")

    __frames_button = Button(
        locator=(By.XPATH, "//span[text()='Frames']"),
        elem_name="Frames Button")

    __web_tables_button = Button(
        locator=(By.XPATH, "//span[text()='Web Tables']"),
        elem_name="Web Tables Button")

    __browser_windows_button = Button(
        locator=(By.XPATH, "//span[text()='Browser Windows']"),
        elem_name="Browser Windows Button")

    __elements_button = Button(
        locator=(By.XPATH, "//div[@class='element-group'][1]"),
        elem_name="Elements Button")

    __links_button = Button(
        locator=(By.XPATH, "//span[text()='Links']"),
        elem_name="Links Button")

    __slider_button = Button(
        locator=(By.XPATH, "//span[text()='Slider']"),
        elem_name="Slider Button")

    __progress_bar_button = Button(
        locator=(By.XPATH, "//span[text()='Progress Bar']"),
        elem_name="Progress Bar Button")

    __date_picker_button = Button(
        locator=(By.XPATH, "//span[text()='Date Picker']"),
        elem_name="Date Picker Button")

    __upload_and_download_button = Button(
        locator=(By.XPATH, "//span[text()='Upload and Download']"),
        elem_name="Upload and Download Button")

    def __init__(self):
        super().__init__(
            unique_element=self.__elements_button,
            name="Panel Form")

    def click_alerts_button(self):
        LoggerUtils().debug("Clicking Alerts Button on the '%s'", self._name)
        self.__alerts_button.click_with_js()

    def click_nested_frames_button(self):
        LoggerUtils().debug("Clicking Nested Frames Button on the '%s'", self._name)
        self.__nested_frames_button.click_with_js()

    def click_frames_button(self):
        LoggerUtils().debug("Clicking Frames Button on the '%s'", self._name)
        self.__frames_button.click_with_js()

    def click_web_tables_button(self):
        LoggerUtils().debug("Clicking Alerts Button on the '%s'", self._name)
        self.__web_tables_button.click()

    def click_browser_windows_button(self):
        LoggerUtils().debug("Clicking Browser Windows Button on the '%s'", self._name)
        self.__browser_windows_button.click_with_js()

    def click_elements_button(self):
        LoggerUtils().debug("Clicking Elements Button on the '%s'", self._name)
        self.__elements_button.click_with_js()

    def click_links_button(self):
        LoggerUtils().debug("Clicking Links Button on the '%s'", self._name)
        self.__links_button.click_with_js()

    def click_upload_and_download_button_with_js(self):
        LoggerUtils().debug("Clicking Upload and Download Button on the '%s'", self._name)
        self.__upload_and_download_button.click_with_js()

    def click_slider_button_with_js(self):
        LoggerUtils().debug("Clicking Slider Button with JS on the '%s'", self._name)
        self.__slider_button.click_with_js()

    def click_progress_bar_button_with_js(self):
        LoggerUtils().debug("Clicking Progress Bar Button with JS on the '%s'", self._name)
        self.__progress_bar_button.click_with_js()

    def click_date_picker_button_with_js(self):
        LoggerUtils().debug("Clicking Date Picker with JS Button on the '%s'", self._name)
        self.__date_picker_button.click_with_js()

    def wait_until_links_button_is_clickable(self):
        LoggerUtils().debug("Waiting until Links Button on the '%s' is clickable", self._name)
        self.__links_button.wait_until_elem_is_clickable()
