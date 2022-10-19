from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Button, Text
from framework.utils.logger_utils import LoggerUtils


class AlertsPage(BaseForm):
    __click_me_to_see_alert_button = Button(
        locator=(By.XPATH, "//button[@id='alertButton']"),
        elem_name="Click-me-to-see-alert Button")

    __click_me_confirm_box_will_appear_button = Button(
        locator=(By.XPATH, "//button[@id='confirmButton']"),
        elem_name="Click-me-and-confirm-box-will-appear Button")

    __click_me_prompt_box_will_appear_button = Button(
        locator=(By.XPATH, "//button[@id='promtButton']"),
        elem_name="Click-me-and-prompt-box-will-appear Button")

    __confirm_box_interaction_result = Text(
        locator=(By.XPATH, "//span[@id='confirmResult']"),
        elem_name="The text displayed after interactions with the confirm box")

    __prompt_box_interaction_result = Text(
        locator=(By.XPATH, "//span[@id='promptResult']"),
        elem_name="The text displayed after interactions with the prompt box")

    def __init__(self):
        super().__init__(
            unique_element=self.__click_me_to_see_alert_button,
            name="Alerts Page")

    def click_to_see_alert_button(self):
        LoggerUtils().debug("Clicking the Button to see an alert on the '%s'", self._name)
        self.__click_me_to_see_alert_button.click()

    def click_to_see_confirm_box(self):
        LoggerUtils().debug("Clicking the Button to see a confirm box on the '%s'", self._name)
        self.__click_me_confirm_box_will_appear_button.click()

    def click_to_see_prompt_box(self):
        LoggerUtils().debug("Clicking the Button to see a prompt box on the '%s'", self._name)
        self.__click_me_prompt_box_will_appear_button.click()

    def get_text_from_confirm_box_interaction_result(self):
        LoggerUtils().debug("Getting text from the Confirm Box Interaction Result Field on the '%s'", self._name)
        return self.__confirm_box_interaction_result.get_text()

    def get_text_from_prompt_box_interaction_result(self):
        LoggerUtils().debug("Getting text from the Prompt Box Interaction Result Field on the '%s'", self._name)
        return self.__prompt_box_interaction_result.get_text()
