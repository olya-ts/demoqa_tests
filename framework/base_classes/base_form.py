from framework.utils.logger_utils import LoggerUtils
from framework.base_classes.base_element import BaseElement


class BaseForm:
    def __init__(self, unique_element: BaseElement, name: str):
        self.__unique_element = unique_element
        self._name = name

    def is_open(self):
        LoggerUtils().debug("Checking if the page '%s' is open", self._name)
        return self.__unique_element.is_present()

    def wait_until_page_is_open(self):
        LoggerUtils().debug("Waiting until the page '%s' opens", self._name)
        self.__unique_element.wait_until_elem_is_visible()
