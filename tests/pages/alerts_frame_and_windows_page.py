from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import DropDownList
from tests.pages.forms.panel_form import PanelForm


class AlertsFrameAndWindowsPage(BaseForm):
    panel_form = PanelForm()

    __dropdown_list_of_alerts_frame_and_windows_button = DropDownList(
        locator=(By.XPATH, "//div[@class='element-group'][3]//child::\
            div[contains(@class, 'element-list')][contains(@class, 'show')]"),
        elem_name="Alerts Frame and Windows Button's DropDown List")

    def __init__(self):
        super().__init__(
            unique_element=self.__dropdown_list_of_alerts_frame_and_windows_button,
            name="Alerts Frame and Windows Page")
