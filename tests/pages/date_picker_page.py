from selenium.webdriver.common.by import By
from framework.base_classes.base_form import BaseForm
from framework.base_classes.elements import TextField, DropDownList, Text, Button
from framework.utils.config_manager import ConfigManager
from framework.utils.other_utils import StringUtils, DateUtils
from framework.utils.logger_utils import LoggerUtils


class DatePickerPage(BaseForm):
    __date_field = TextField(
        locator=(By.XPATH, "//input[@id='datePickerMonthYearInput']"),
        elem_name="Date Field")

    __date_and_time_field = TextField(
        locator=(By.XPATH, "//input[@id='dateAndTimePickerInput']"),
        elem_name="Date and Time Field")

    __month_selector = DropDownList(
        locator=(By.XPATH, "//div[contains(@class, 'react-datepicker__month-dropdown-container')]"),
        elem_name="Month Selector")

    __year_selector = DropDownList(
        locator=(By.XPATH, "//div[contains(@class, 'react-datepicker__year-dropdown-container')]"),
        elem_name="Year Selector")

    __month_option = Text(
        locator=(By.XPATH, f"//option[text()='{ConfigManager.get_test_data()['month']}']"),
        elem_name="Month Option")

    __calendar_dates = Button(
        locator=(
            By.XPATH,
            "//div[@class='react-datepicker__week']//child::div[contains(@class, 'react-datepicker__day')]"),
        elem_name="Calendar Dates")

    __date = Button(
        locator=(By.XPATH, f"//div[text()='{ConfigManager.get_test_data()['date']}']\
            [contains(@aria-label, '{ConfigManager.get_test_data()['month']}')]"),
        elem_name="Date")

    __selected_month_and_year = Text(
        locator=(By.XPATH, "//div[contains(@class, 'react-datepicker__current-month')]"),
        elem_name="Selected Month and Date")

    def __init__(self):
        super().__init__(
            unique_element=self.__date_field,
            name="Date Picker Page")

    def click_date_field(self):
        LoggerUtils().debug("Clicking on the Date Field on the '%s'", self._name)
        self.__date_field.click()

    def click_month_selector(self):
        LoggerUtils().debug("Clicking on the Month Selector on the '%s'", self._name)
        self.__month_selector.click()

    def click_year_selector(self):
        LoggerUtils().debug("Clicking on the Year Selector on the '%s'", self._name)
        self.__year_selector.click()

    def choose_month(self):
        LoggerUtils().debug("Clicking on the Month Option on the '%s'", self._name)
        self.__month_option.click()

    def get_date_from_date_field(self):
        LoggerUtils().debug("Getting value of the Date Field attribute on the '%s'", self._name)
        return self.__date_field.get_attribute("value")

    def get_date_time_from_date_and_time_field(self):
        LoggerUtils().debug("Getting value of the Date and Time Field attribute on the '%s'", self._name)
        return self.__date_and_time_field.get_attribute("value")

    def get_selected_month_and_year(self):
        LoggerUtils().debug("Getting text from the Selected Month and Year Field on the '%s'", self._name)
        return self.__selected_month_and_year.get_text()

    def check_if_date_is_in_the_calendar(self):
        LoggerUtils().debug("Checking if the target date is in the calendar on the '%s'", self._name)
        return True if self.__date.is_present() else False

    def choose_date(self):
        LoggerUtils().debug("Clicking on the Date Field on the '%s'", self._name)
        self.__date.click_with_js()

    def choose_one_year_after(self):
        LoggerUtils().debug("Choosing the follwoing year with the down arrow on the '%s'", self._name)
        self.__year_selector.press_down_arrow()
        self.__year_selector.press_enter()

    def select_year_that_has_target_date(self):
        LoggerUtils().debug("Looking for the year that has the target date on the '%s'", self._name)
        while self.check_if_date_is_in_the_calendar() is False:
            self.click_year_selector()
            self.choose_one_year_after()

    def get_selected_month_date_year(self):
        LoggerUtils().debug("Returning the selected month, date and year on the '%s'", self._name)
        date = str(ConfigManager.get_test_data()["date"])
        selected_month = DateUtils.convert_month_to_number(
            StringUtils.get_str_without_digits(self.get_selected_month_and_year()))
        selected_year = str(StringUtils.get_int_from_str(self.get_selected_month_and_year()))
        return selected_month + "/" + date + "/" + selected_year
