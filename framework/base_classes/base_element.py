from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from framework.driver.web_driver import WebDriver
from framework.utils.wait_utils import WaitUtils
from framework.utils.logger_utils import LoggerUtils
from framework.utils.driver_utils import DriverUtils


class BaseElement:
    def __init__(self, locator: tuple, elem_name: str):
        self.__locator = locator
        self._name = elem_name

    def _find_element(self):
        LoggerUtils().debug("Finding the element '%s'", self._name)
        return WebDriver().find_element(*self.__locator)

    def _find_elements(self):
        LoggerUtils().debug("Finding elements '%s'", self._name)
        return WebDriver().find_elements(*self.__locator)

    def get_number_of_elements(self):
        LoggerUtils().debug("Getting the number of elements '%s'", self._name)
        return len(self._find_elements())

    def is_present(self):
        LoggerUtils().debug("Checking if the element '%s' is present", self._name)
        return True if self._find_elements() else False

    def click(self):
        LoggerUtils().debug("Clicking on the element '%s'", self._name)
        self._find_element().click()

    def move_to(self):
        LoggerUtils().debug("Moving to the element '%s'", self._name)
        ActionChains(WebDriver()).move_to_element(self._find_element()).perform()

    def scroll_to(self):
        LoggerUtils().debug("Scrolling to the element '%s'", self._name)
        ActionChains(WebDriver()).scroll_to_element(self._find_element()).perform()

    def click_with_js(self):
        LoggerUtils().debug("Clicking on the element '%s' by means of javascript", self._name)
        DriverUtils.execute_click(self._find_element())

    def get_text(self):
        LoggerUtils().debug("Getting text from the element '%s'", self._name)
        return self._find_element().text

    def get_attribute(self, attribute_name):
        LoggerUtils().debug("Getting text from the element's '%s' attribute '%s'", self._name, attribute_name)
        return self._find_element().get_attribute(attribute_name)

    def is_displayed(self):
        LoggerUtils().debug("Checking if the element '%s' is displayed", self._name)
        try:
            if self._find_element().is_displayed():
                return True
        except NoSuchElementException:
            LoggerUtils().exception("The element %s is not found", self._name)
            return False

    def wait_until_elem_is_visible(self):
        LoggerUtils().debug("Waiting for the element '%s' to be visible", self._name)
        WaitUtils.wait_until_elem_is_visible(self.__locator)

    def wait_until_elem_is_looked_for_more_often(self):
        LoggerUtils().debug("Waiting for the element '%s' to be visible", self._name)
        WaitUtils.wait_until_elem_is_visible_checking_more_often(self.__locator)

    def wait_until_elem_is_invisible(self):
        LoggerUtils().debug("Waiting for the element '%s' to be invisible", self._name)
        WaitUtils.wait_until_elem_is_invisible(self.__locator)

    def wait_until_elem_is_clickable(self):
        LoggerUtils().debug("Waiting for the element '%s' to be clickable", self._name)
        WaitUtils.wait_until_elem_is_clickable(self._find_element())

    @staticmethod
    def press_left_arrow():
        LoggerUtils().debug("Pressing the left arrow key on the keyboard")
        ActionChains(WebDriver()).key_down(Keys.LEFT).key_up(Keys.LEFT).perform()

    @staticmethod
    def press_right_arrow():
        LoggerUtils().debug("Pressing the right  arrow key on the keyboard")
        ActionChains(WebDriver()).key_down(Keys.RIGHT).key_up(Keys.RIGHT).perform()

    @staticmethod
    def press_down_arrow():
        LoggerUtils().debug("Pressing the up arrow key on the keyboard")
        ActionChains(WebDriver()).key_down(Keys.DOWN).key_up(Keys.DOWN).perform()

    @staticmethod
    def press_enter():
        LoggerUtils().debug("Pressing the up arrow key on the keyboard")
        ActionChains(WebDriver()).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
