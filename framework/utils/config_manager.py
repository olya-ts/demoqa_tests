import json
from framework.utils.logger_utils import LoggerUtils


class ConfigManager:
    @staticmethod
    def get_config_data():
        LoggerUtils().debug("Reading from the config.json file")
        with open(r'tests/data/config.json') as config_file:
            data = json.load(config_file)
        return data

    @staticmethod
    def get_test_data():
        LoggerUtils().debug("Reading from the test_data.json file")
        with open(r'tests/data/test_data.json') as test_data_file:
            data = json.load(test_data_file)
        return data

    @staticmethod
    def get_user_data():
        LoggerUtils().debug("Reading from the user_data.json file")
        with open(r'tests/data/user_data.json') as user_data:
            data = json.load(user_data)
        return data
