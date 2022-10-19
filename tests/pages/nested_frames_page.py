from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Text
from framework.utils.driver_utils import DriverUtils
from tests.pages.forms.panel_form import PanelForm
from framework.utils.logger_utils import LoggerUtils


class NestedFramesPage(BaseForm):
    panel_form = PanelForm()

    __parent_frame_body = Text(
        locator=(By.XPATH, "//body"),
        elem_name="Parent Frame's text")

    __child_iframe_paragraph = Text(
        locator=(By.XPATH, "//p"),
        elem_name="Child Frame's text")

    __description_of_nested_frames_page = Text(
        locator=(By.XPATH, "//div[@id='framesWrapper']//child::div[not(contains(@id, 'frame1Wrapper'))]"),
        elem_name="The Nested Frames Page's Description")

    def __init__(self):
        super().__init__(
            unique_element=self.__description_of_nested_frames_page,
            name="Nested Frames Page")

    def switch_to_the_parent_frame(self):
        LoggerUtils().debug("Switching to the parent frame on the '%s'", self._name)
        DriverUtils.switch_to_frame(by=By.ID, frame="frame1", name="parent frame")

    def switch_to_the_child_frame(self):
        LoggerUtils().debug("Switching to the child frame on the '%s'", self._name)
        DriverUtils.switch_to_frame(by=By.TAG_NAME, frame="iframe", name="child frame")

    def get_text_from_parent_frame(self):
        LoggerUtils().debug("Getting text from the parent frame on the '%s'", self._name)
        return self.__parent_frame_body.get_text()

    def get_text_from_child_iframe(self):
        LoggerUtils().debug("Getting text from the child frame on the '%s'", self._name)
        return self.__child_iframe_paragraph.get_text()
