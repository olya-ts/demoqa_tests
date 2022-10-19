from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import Button, TextField, Text
from framework.utils.logger_utils import LoggerUtils


class WebTablesPage(BaseForm):
    __parameterized_locator_base_part = \
        "//div[text()='{text_value}']//following-sibling::div[@role='gridcell']//child::span[@title='Delete']"
    __add_button = Button(
        locator=(By.XPATH, "//button[@id='addNewRecordButton']"),
        elem_name="Add Button")

    __submit_button = Button(
        locator=(By.XPATH, "//button[@id='submit']"),
        elem_name="Submit Button")

    __first_name_input_field = TextField(
        locator=(By.XPATH, "//input[@id='firstName']"),
        elem_name="First Name Input Field")

    __last_name_input_field = TextField(
        locator=(By.XPATH, "//input[@id='lastName']"),
        elem_name="Last Name Input Field")

    __email_input_field = TextField(
        locator=(By.XPATH, "//input[@id='userEmail']"),
        elem_name="Email Input Field")

    __age_input_field = TextField(
        locator=(By.XPATH, "//input[@id='age']"),
        elem_name="Age Input Field")

    __salary_input_field = TextField(
        locator=(By.XPATH, "//input[@id='salary']"),
        elem_name="Salary Input Field")

    __department_input_field = TextField(
        locator=(By.XPATH, "//input[@id='department']"),
        elem_name="Department Input Field")

    __first_name_table_cell = Text(
        locator=(By.XPATH, "(//div[@role='row'])[5]//child::div[@role='gridcell'][1]"),
        elem_name="First Name Table Cell"
    )

    __last_name_table_cell = Text(
        locator=(By.XPATH, "(//div[@role='row'])[5]//child::div[@role='gridcell'][2]"),
        elem_name="Last Name Table Cell"
    )

    __age_table_cell = Text(
        locator=(By.XPATH, "(//div[@role='row'])[5]//child::div[@role='gridcell'][3]"),
        elem_name="Age Table Cell"
    )

    __email_table_cell = Text(
        locator=(By.XPATH, "(//div[@role='row'])[5]//child::div[@role='gridcell'][4]"),
        elem_name="Email Table Cell"
    )

    __salary_table_cell = Text(
        locator=(By.XPATH, "(//div[@role='row'])[5]//child::div[@role='gridcell'][5]"),
        elem_name="Salary Table Cell"
    )

    __department_table_cell = Text(
        locator=(By.XPATH, "(//div[@role='row'])[5]//child::div[@role='gridcell'][6]"),
        elem_name="Department Table Cell"
    )

    __action_buttons = Button(
        locator=(By.XPATH, "//div[@class='action-buttons']"),
        elem_name="Action Buttons"
    )

    def __init__(self):
        super().__init__(
            unique_element=self.__add_button,
            name="Web Tables Page")

    def click_add_button(self):
        LoggerUtils().debug("Clicking Add Button on the '%s'", self._name)
        self.__add_button.click()

    def click_submit_button(self):
        LoggerUtils().debug("Clicking Submit Button on the '%s'", self._name)
        self.__submit_button.click()

    def click_delete_record_button(self, record):
        LoggerUtils().debug("Clicking Delete Record Button on the '%s'", self._name)
        delete_button = Button(
            locator=(By.XPATH, self.__parameterized_locator_base_part.format(text_value=record)),
            elem_name="Delete Button"
        )
        delete_button.click()

    def check_if_registration_form_is_open(self):
        LoggerUtils().debug("Checking if Submit Button is present on the '%s'", self._name)
        return self.__submit_button.is_present()

    def send_text_to_first_name_input_field(self, text):
        LoggerUtils().debug("Sending text to the First Name Input Field on the '%s'", self._name)
        self.__first_name_input_field.send_text(text)

    def send_text_to_last_name_input_field(self, text):
        LoggerUtils().debug("Sending text to the Last Name Input Field on the '%s'", self._name)
        self.__last_name_input_field.send_text(text)

    def send_text_to_email_input_field(self, text):
        LoggerUtils().debug("Sending text to the Email Input Field on the '%s'", self._name)
        self.__email_input_field.send_text(text)

    def send_text_to_age_input_field(self, text):
        LoggerUtils().debug("Sending text to the Age Input Field on the '%s'", self._name)
        self.__age_input_field.send_text(text)

    def send_text_to_salary_input_field(self, text):
        LoggerUtils().debug("Sending text to the Salary Input Field on the '%s'", self._name)
        self.__salary_input_field.send_text(text)

    def send_text_to_department_input_field(self, text):
        LoggerUtils().debug("Sending text to the Department Input Field on the '%s'", self._name)
        self.__department_input_field.send_text(text)

    def get_text_from_first_name_table_cell(self):
        LoggerUtils().debug("Getting text from the First Name Table cell on the '%s'", self._name)
        return self.__first_name_table_cell.get_text()

    def get_text_from_last_name_table_cell(self):
        LoggerUtils().debug("Getting text from the Last Name Table cell on the '%s'", self._name)
        return self.__last_name_table_cell.get_text()

    def get_text_from_age_table_cell(self):
        LoggerUtils().debug("Getting text from the Age Table cell on the '%s'", self._name)
        return self.__age_table_cell.get_text()

    def get_text_from_email_table_cell(self):
        LoggerUtils().debug("Getting text from the Email Table cell on the '%s'", self._name)
        return self.__email_table_cell.get_text()

    def get_text_from_salary_table_cell(self):
        LoggerUtils().debug("Getting text from the Salary Table cell on the '%s'", self._name)
        return self.__salary_table_cell.get_text()

    def get_text_from_department_table_cell(self):
        LoggerUtils().debug("Getting text from the Department Table cell on the '%s'", self._name)
        return self.__department_table_cell.get_text()

    def wait_until_submit_button_is_invisible(self):
        LoggerUtils().debug("Waiting until Submit Button is invisible on the '%s'", self._name)
        self.__submit_button.wait_until_elem_is_invisible()

    def check_if_submit_button_is_displayed(self):
        LoggerUtils().debug("Checking if Submit Button is displayed on the '%s'", self._name)
        return self.__submit_button.is_displayed()

    def get_number_of_table_records(self):
        LoggerUtils().debug("Getting a number of table records on the '%s'", self._name)
        return self.__action_buttons.get_number_of_elements()
