from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Button
from tests.pages.forms.panel_form import PanelForm
from framework.utils.logger_utils import LoggerUtils


class BrowserWindowsPage(BaseForm):
    panel_form = PanelForm()

    __new_tab_button = Button(
        locator=(By.XPATH, "//button[@id='tabButton']"),
        elem_name="New Tab Button")

    def __init__(self):
        super().__init__(
            unique_element=self.__new_tab_button,
            name="Browser Windows Page")

    def click_new_tab_button(self):
        LoggerUtils().debug("Clicking New Tab Button on the '%s'", self._name)
        self.__new_tab_button.click()
