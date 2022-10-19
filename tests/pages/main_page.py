from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Button
from framework.utils.logger_utils import LoggerUtils


class MainPage(BaseForm):
    __alerts_frame_and_windows_button = Button(
        locator=(By.XPATH, "//div[@class='card-body']//child::*[text()='Alerts, Frame & Windows']"),
        elem_name="Alerts Frame and Windows Button")

    __elements_button = Button(
        locator=(By.XPATH, "//div[@class='card-body']//child::*[text()='Elements']"),
        elem_name="Elements Button")

    __widgets_button = Button(
        locator=(By.XPATH, "//div[@class='card-body']//child::*[text()='Widgets']"),
        elem_name="Widgets Button")

    __selenium_certification_training_button = Button(
        locator=(By.XPATH, "//img[@class='banner-image']"),
        elem_name="Selenium Certification training Button")

    def __init__(self):
        super().__init__(
            unique_element=MainPage.__selenium_certification_training_button,
            name="Main Page")

    def click_alerts_frame_and_windows_button(self):
        LoggerUtils().debug("Clicking Alerts Frame and Windows Button on the '%s'", self._name)
        self.__alerts_frame_and_windows_button.click_with_js()

    def click_elements_button(self):
        LoggerUtils().debug("Clicking Elements Button on the '%s'", self._name)
        self.__elements_button.click_with_js()

    def click_widgets_button(self):
        LoggerUtils().debug("Clicking Widgets Button on the '%s'", self._name)
        self.__widgets_button.click_with_js()
