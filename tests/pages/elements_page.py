from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import DropDownList
from tests.pages.forms.panel_form import PanelForm


class ElementsPage(BaseForm):
    panel_form = PanelForm()

    __drop_down_list_of_element_button = DropDownList(
        locator=(By.XPATH, "//div[@class='element-group'][1]//child::\
            div[contains(@class, 'element-list')][contains(@class, 'show')]"),
        elem_name="Elements Button's Drop-down List")

    def __init__(self):
        super().__init__(
            unique_element=self.__drop_down_list_of_element_button,
            name="Elements Page")
