from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Button, TextField
from framework.utils.logger_utils import LoggerUtils
from framework.utils.config_manager import ConfigManager


class UploadAndDownloadPage(BaseForm):
    __download_button = Button(
        locator=(By.XPATH, "//a[@id='downloadButton']"),
        elem_name="Download Button")

    __choose_file = TextField(
        locator=(By.XPATH, "//input[@id='uploadFile']"),
        elem_name="Choose File Text Field")

    __uploaded_path = TextField(
        locator=(By.XPATH, "//p[@id='uploadedFilePath']"),
        elem_name="Uploaded Path")

    def __init__(self):
        super().__init__(
            unique_element=self.__download_button,
            name="Upload and Download Page")

    def click_download_button(self):
        LoggerUtils().debug("Clicking Download Button on the '%s'", self._name)
        self.__download_button.click()

    def click_choose_file_field(self):
        LoggerUtils().debug("Clicking Choose File Field on the '%s'", self._name)
        self.__choose_file.click()

    def send_file_path_to_choose_file_field(self):
        LoggerUtils().debug("Sending the file path to Choose File Field on the '%s'", self._name)
        self.__choose_file.send_text(ConfigManager.get_config_data()["default_directory"]
                                     + ConfigManager.get_test_data()["file"])

    def get_text_from_uploaded_path(self):
        LoggerUtils().debug("Getting text from Uploaded Path Field on the '%s'", self._name)
        return self.__uploaded_path.get_text()
