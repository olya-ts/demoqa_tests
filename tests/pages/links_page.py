from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Text, Link
from framework.utils.logger_utils import LoggerUtils


class LinksPage(BaseForm):
    __link_to_home_page = Link(
        locator=(By.XPATH, "//a[@id='simpleLink']"),
        elem_name="Link to Home Page")

    __description_of_links = Text(
        locator=(By.XPATH, "(//strong)[1]"),
        elem_name="Links' Description")

    def __init__(self):
        super().__init__(
            unique_element=self.__description_of_links,
            name="Links Page")

    def click_link_to_home_page(self):
        LoggerUtils().debug("Clicking on the Home Page Link on the '%s'", self._name)
        self.__link_to_home_page.click()
