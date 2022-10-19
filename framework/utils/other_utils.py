import random
import string
from datetime import datetime
import os
from framework.utils.config_manager import ConfigManager
from framework.utils.logger_utils import LoggerUtils


class RandomUtils:
    @staticmethod
    def generate_random_string():
        LoggerUtils().debug("Generating a random string")
        str_length = ConfigManager.get_test_data()["random_string_length"]
        return ''.join(random.choices(string.ascii_letters, k=str_length))

    @staticmethod
    def generate_random_int():
        LoggerUtils().debug("Generating a random integer")
        min_value = ConfigManager.get_test_data()["slider_min_value"]
        max_value = ConfigManager.get_test_data()["slider_max_value"]
        return random.randint(min_value, max_value)


class StringUtils:
    @staticmethod
    def get_int_from_str(input_string):
        LoggerUtils().debug("Getting an integer from a string")
        for elem in input_string:
            if not elem.isdigit():
                input_string = input_string.replace(elem, "")
        return int(input_string)

    @staticmethod
    def get_str_without_digits(input_string):
        LoggerUtils().debug("Getting a string with no digits")
        for elem in input_string:
            if not elem.isalpha():
                input_string = input_string.replace(elem, "")
        return input_string


class DateUtils:
    @staticmethod
    def get_current_date_time(my_format):
        LoggerUtils().debug("Getting a current date and time")
        return datetime.strftime(datetime.today(), my_format)

    @staticmethod
    def convert_month_to_number(month):
        LoggerUtils().debug("Converting a month to a corresponding number")
        return str(datetime.strptime(month, '%B').month).zfill(2)


class FileUtils:
    @staticmethod
    def check_if_directory_is_empty(path):
        LoggerUtils().debug("Checking if a directory is empty")
        return True if os.listdir(path) else False

    @staticmethod
    def check_if_file_is_downloaded(path, file_name):
        LoggerUtils().debug("Checking if a file '%s' is downloaded", file_name)
        file_path = path + file_name
        flag = False
        while flag is False:
            if os.path.exists(file_path):
                flag = True
                break
