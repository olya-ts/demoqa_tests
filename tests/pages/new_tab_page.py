from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Text


class NewTabPage(BaseForm):
    __heading_of_new_tab_page = Text(
        locator=(By.XPATH, "//*[@id='sampleHeading']"),
        elem_name="Heading of the New Tab Page")

    def __init__(self):
        super().__init__(
            unique_element=self.__heading_of_new_tab_page,
            name="New Tab Page")
