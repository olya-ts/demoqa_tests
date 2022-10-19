from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import DropDownList
from tests.pages.forms.panel_form import PanelForm


class WidgetsPage(BaseForm):
    panel_form = PanelForm()

    __drop_down_list_of_widgets_button = DropDownList(
        locator=(By.XPATH, "//div[@class='element-group'][4]//child::\
            div[contains(@class, 'element-list')][contains(@class, 'show')]"),
        elem_name="Widgets Button's Drop-down List")

    def __init__(self):
        super().__init__(
            unique_element=self.__drop_down_list_of_widgets_button,
            name="Widgets Page")
