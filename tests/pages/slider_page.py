from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Slider, Label, TextField
from tests.pages.forms.panel_form import PanelForm
from framework.utils.logger_utils import LoggerUtils


class SliderPage(BaseForm):
    panel_form = PanelForm()

    __slider = Slider(
        locator=(By.XPATH, "//input[@type='range']"),
        elem_name="Slider")

    __slider_label = Label(
        locator=(By.XPATH, "//div[@class='range-slider__tooltip__label']"),
        elem_name="Slider Label")

    __slider_value_field = TextField(
        locator=(By.XPATH, "//input[@id='sliderValue']"),
        elem_name="Slider Value Field")

    def __init__(self):
        super().__init__(
            unique_element=self.__slider,
            name="Slider Page")

    def click_slider(self):
        LoggerUtils().debug("Clicking on the Slider on the '%s'", self._name)
        self.__slider.click()

    def wait_until_slider_label_text_is_visible(self):
        LoggerUtils().debug("Waiting until Slider Label text is visible on the '%s'", self._name)
        flag = True
        while len(self.__slider_label.get_text()) == 0:
            flag = False

    def set_slider_value(self, value):
        LoggerUtils().debug("Setting Slider value on the '%s'", self._name)
        self.__slider.set_slider(self.__slider_label, value)

    def get_slider_value(self):
        LoggerUtils().debug("Getting value of the Slider attribute on the '%s'", self._name)
        return self.__slider.get_attribute("value")

    def get_value_from_slider_value_field(self):
        LoggerUtils().debug("Getting value of the Slider Value Field's attribute on the '%s'", self._name)
        return self.__slider_value_field.get_attribute("value")
