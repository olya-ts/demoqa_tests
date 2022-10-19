from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from framework.utils.config_manager import ConfigManager
from framework.utils.logger_utils import LoggerUtils


class BrowserFactory:
    @staticmethod
    def get_driver():
        LoggerUtils().debug("Downloading the browser driver and configuring it")
        if ConfigManager.get_config_data()["browser"] == "Chrome":
            service = Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            for browser_option in ConfigManager.get_config_data()["browser_options"]:
                options.add_argument(browser_option)
            try:
                if ConfigManager.get_config_data()["default_directory"]:
                    prefs = {"download.default_directory": ConfigManager.get_config_data()["default_directory"]}
                    options.add_experimental_option("prefs", prefs)
            except KeyError:
                LoggerUtils().warning("Default directory is not set")
            return webdriver.Chrome(service=service, options=options)

        elif ConfigManager.get_config_data()["browser"] == "Microsoft Edge":
            service = Service(EdgeChromiumDriverManager().install())
            options = webdriver.EdgeOptions()
            for browser_option in ConfigManager.get_config_data()["browser_options"]:
                options.add_argument(browser_option)
            try:
                if ConfigManager.get_config_data()["default_directory"]:
                    prefs = {"download.default_directory": ConfigManager.get_config_data()["default_directory"]}
                    options.add_experimental_option("prefs", prefs)
            except KeyError:
                LoggerUtils().warning("Default directory is not set")
            return webdriver.Edge(service=service, options=options)

        else:
            LoggerUtils().critical("The browser name '%s' is not valid", ConfigManager.get_config_data()['browser'])
            raise Exception(f"The browser name {ConfigManager.get_config_data()['browser']} is not valid")
