from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Text
from framework.utils.driver_utils import DriverUtils
from framework.utils.logger_utils import LoggerUtils


class FramesPage(BaseForm):
    __upper_frame_heading = Text(
        locator=(By.XPATH, "//h1[@id='sampleHeading']"),
        elem_name="Upper-frame heading")

    __lower_frame_heading = Text(
        locator=(By.XPATH, "//h1[@id='sampleHeading']"),
        elem_name="Lower-frame heading")

    __description_of_frames_page = Text(
        locator=(By.XPATH, "//div[@id='framesWrapper']//child::div[not(contains(@id, 'frame1Wrapper')) \
            and not(contains(@id, 'frame2Wrapper'))]"),
        elem_name="Frames Page Description")

    def __init__(self):
        super().__init__(
            unique_element=self.__description_of_frames_page,
            name="Frames Page")

    def switch_to_the_upper_frame(self):
        LoggerUtils().debug("Switching to the upper frame on the '%s'", self._name)
        DriverUtils.switch_to_frame(by=By.ID, frame="frame1", name="frame1")

    def switch_to_the_lower_frame(self):
        LoggerUtils().debug("Switching to the lower frame on the '%s'", self._name)
        DriverUtils.switch_to_frame(by=By.ID, frame="frame2", name="frame2")

    def get_text_from_the_upper_frame(self):
        LoggerUtils().debug("Getting text from the upper frame on the '%s'", self._name)
        return self.__upper_frame_heading.get_text()

    def get_text_from_the_lower_frame(self):
        LoggerUtils().debug("Getting text from the lower frame on the '%s'", self._name)
        return self.__lower_frame_heading.get_text()
