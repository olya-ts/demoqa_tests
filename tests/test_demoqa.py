import pytest
from tests.pages.main_page import MainPage
from tests.pages.alerts_page import AlertsPage
from tests.pages.alerts_frame_and_windows_page import AlertsFrameAndWindowsPage
from tests.pages.nested_frames_page import NestedFramesPage
from tests.pages.frames_page import FramesPage
from tests.pages.elements_page import ElementsPage
from tests.pages.web_tables_page import WebTablesPage
from tests.pages.browser_windows_page import BrowserWindowsPage
from tests.pages.new_tab_page import NewTabPage
from tests.pages.links_page import LinksPage
from tests.pages.widgets_page import WidgetsPage
from tests.pages.slider_page import SliderPage
from tests.pages.progress_bar_page import ProgressBarPage
from tests.pages.date_picker_page import DatePickerPage
from tests.pages.upload_and_download_page import UploadAndDownloadPage
from framework.utils.wait_utils import WaitUtils
from framework.utils.other_utils import RandomUtils, DateUtils, FileUtils
from framework.utils.driver_utils import DriverUtils
from framework.utils.config_manager import ConfigManager
from framework.utils.logger_utils import LoggerUtils


class TestAlerts:
    def test_alerts_on_the_alerts_page(self, maximize_window, quit_driver):
        LoggerUtils().info("Step 1. Navigating to the Main Page and checking if it is open")
        DriverUtils.navigate(ConfigManager.get_config_data()["url"])
        main_page = MainPage()
        main_page.wait_until_page_is_open()
        assert main_page.is_open(), "It's not Main Page as the unique element is not found"

        LoggerUtils().info("Step 2. Clicking on the Alerts Frame and Windows Button. "
                           "Then clicking on the Alerts Button on the panel. Checking if the Alerts Page is open")
        main_page.click_alerts_frame_and_windows_button()
        alerts_frame_and_windows_page = AlertsFrameAndWindowsPage()
        alerts_frame_and_windows_page.panel_form.click_alerts_button()
        alerts_page = AlertsPage()
        alerts_page.wait_until_page_is_open()
        assert alerts_page.is_open(), "It's not Alerts Page as the unique element is not found"

        LoggerUtils().info("Step 3. Clicking on the Click-me-to-see-alert Button. "
                           "Checking if the alert appears")
        alerts_page.click_to_see_alert_button()
        alert = WaitUtils.wait_until_alert_is_present()
        assert alert.text == ConfigManager.get_test_data()["alert_text"], \
            "The alert with the expected text hasn't appeared"

        LoggerUtils().info("Step 4. Clicking the Ok button on the Alert and checking if the alert closes")
        alert.accept()
        assert DriverUtils.check_if_alert_is_on_page() is False, "Alert is not closed"

        LoggerUtils().info("Step 5. Clicking on the Click-me-and-confirm-box-appears Button. "
                           "Checking if the confirm box appears")
        alerts_page.click_to_see_confirm_box()
        confirm_box = WaitUtils.wait_until_alert_is_present()
        assert confirm_box.text == ConfigManager.get_test_data()["confirm_box_text"], \
            "The confirm box with the expected text hasn't appeared"

        LoggerUtils().info("Step 6. Clicking the Ok button on the confirm box. "
                           "Checking if the confirm box closes and if the text appears on the page")
        confirm_box.accept()
        assert DriverUtils.check_if_alert_is_on_page() is False, "Confirm box is not closed"
        assert alerts_page.get_text_from_confirm_box_interaction_result() == \
               ConfigManager.get_test_data()["close_confirm_box_text"], "The expected_text hasn't appeared"

        LoggerUtils().info("Step 7. Clicking on the Click-me-and-prompt-box-appears Button. "
                           "Checking if the prompt box appears")
        alerts_page.click_to_see_prompt_box()
        prompt = WaitUtils.wait_until_alert_is_present()
        assert prompt.text == ConfigManager.get_test_data()["prompt_box_text"],\
            "The prompt box with the expected text hasn't appeared"

        LoggerUtils().info("Step 8. Entering randomly generated text and clicking Ok on the prompt box. "
                           "Checking if the prompt box closes and if the entered text appears on the page")
        input_text = RandomUtils.generate_random_string()
        prompt.send_keys(input_text)
        prompt.accept()
        assert DriverUtils.check_if_alert_is_on_page() is False, "Prompt is not closed"
        assert input_text in alerts_page.get_text_from_prompt_box_interaction_result(), \
            "Appeared text doesn't equal to the entered text"


class TestFrames:
    def test_frames_on_the_frames_and_nested_frames_pages(self, maximize_window, quit_driver):
        LoggerUtils().info("Step 1. Navigating to the Main Page and checking if it is open")
        DriverUtils.navigate(ConfigManager.get_config_data()["url"])
        main_page = MainPage()
        main_page.wait_until_page_is_open()
        assert main_page.is_open(), "It's not Main Page as the unique element is not found"

        LoggerUtils().info("Step 2. Clicking on the Alerts Frame and Windows Button. "
                           "Then clicking Nested Frames Button on the panel. "
                           "Checking if the Nested Frames Page is open. "
                           "Checking if there are messages present on the page")
        main_page.click_alerts_frame_and_windows_button()
        alerts_frame_and_windows_page = AlertsFrameAndWindowsPage()
        alerts_frame_and_windows_page.panel_form.click_nested_frames_button()
        nested_frames_page = NestedFramesPage()
        nested_frames_page.wait_until_page_is_open()
        assert nested_frames_page.is_open(), "It's not Nested Frames Page as the unique element is not found"
        nested_frames_page.switch_to_the_parent_frame()
        assert nested_frames_page.get_text_from_parent_frame() == ConfigManager.get_test_data()["parent_frame_text"], \
            "The expected message of the parent frame isn't present on the page"
        nested_frames_page.switch_to_the_child_frame()
        assert nested_frames_page.get_text_from_child_iframe() == ConfigManager.get_test_data()["child_frame_text"], \
            "The expected message of the child frame isn't present on the page"

        LoggerUtils().info("Step 3. Clicking Frames Button on the panel. Checking if the Frames Page is open. "
                           "Checking if the message from the upper frame equals to the message from the lower frame")
        DriverUtils.switch_back_from_frame()
        nested_frames_page.panel_form.click_frames_button()
        frames_page = FramesPage()
        frames_page.wait_until_page_is_open()
        assert frames_page.is_open(), "It's not Frames Page as the unique element is not found"
        frames_page.switch_to_the_upper_frame()
        upper_frame_text = frames_page.get_text_from_the_upper_frame()
        DriverUtils.switch_back_from_frame()
        frames_page.switch_to_the_lower_frame()
        lower_frame_text = frames_page.get_text_from_the_lower_frame()
        assert upper_frame_text == lower_frame_text, \
            "The message from the upper frame doesn't equal to the message from the lower frame"


class TestTables:
    @pytest.mark.parametrize("user_data", ConfigManager.get_user_data().values())
    def test_tables_on_the_web_tables_page(self, maximize_window, quit_driver, user_data):
        LoggerUtils().info("Step 1. Navigating to the Main Page and checking if it is open")
        DriverUtils.navigate(ConfigManager.get_config_data()["url"])
        main_page = MainPage()
        main_page.wait_until_page_is_open()
        assert main_page.is_open(), "It's not Main Page as the unique element is not found"

        LoggerUtils().info("Step 2. Clicking on the Elements Button. "
                           "Then clicking on the Web Tables Button on the panel. "
                           "Checking if the Web Tables Page is open")
        main_page.click_elements_button()
        elements_page = ElementsPage()
        elements_page.panel_form.click_web_tables_button()
        web_tables_page = WebTablesPage()
        assert web_tables_page.is_open(), "It's not Web Tables Page as the unique element is not found"

        LoggerUtils().info("Step 3. Clicking on the Add Button. "
                           "Checking if the Registration Form has appeared")
        web_tables_page.click_add_button()
        assert web_tables_page.check_if_registration_form_is_open(), "The Registration Form isn't open"

        LoggerUtils().info("Step 4. Entering test data to the table and clicking the Submit Button. "
                           "Checking if the Registration form has closed and if the entered data is in the table")
        web_tables_page.send_text_to_first_name_input_field(user_data["first_name"])
        web_tables_page.send_text_to_last_name_input_field(user_data["last_name"])
        web_tables_page.send_text_to_email_input_field(user_data["email"])
        web_tables_page.send_text_to_age_input_field(user_data["age"])
        web_tables_page.send_text_to_salary_input_field(user_data["salary"])
        web_tables_page.send_text_to_department_input_field(user_data["department"])
        web_tables_page.click_submit_button()
        web_tables_page.wait_until_submit_button_is_invisible()
        assert web_tables_page.check_if_submit_button_is_displayed() is False, "The Registration Form isn't closed"
        assert web_tables_page.get_text_from_first_name_table_cell() == user_data["first_name"], \
            "The first name hasn't appeared in the table"
        assert web_tables_page.get_text_from_last_name_table_cell() == user_data["last_name"], \
            "The last name hasn't appeared in the table"
        assert web_tables_page.get_text_from_age_table_cell() == user_data["age"], \
            "The age hasn't appeared in the table"
        assert web_tables_page.get_text_from_email_table_cell() == user_data["email"], \
            "The email hasn't appeared in the table"
        assert web_tables_page.get_text_from_salary_table_cell() == user_data["salary"], \
            "The salary hasn't appeared in the table"
        assert web_tables_page.get_text_from_department_table_cell() == user_data["department"], \
            "The department hasn't appeared in the table "

        LoggerUtils().info("Step 5. Deleting user's data from the table. "
                           "Checking if the number of records in the table has changed and if the data is deleted")
        records_num_before = web_tables_page.get_number_of_table_records()
        web_tables_page.click_delete_record_button(user_data["email"])
        record_num_after = web_tables_page.get_number_of_table_records()
        assert records_num_before != record_num_after, "The number of records hasn't changed"


class TestHandles:
    def test_handles_on_the_browser_windows__and_links_pages(self, maximize_window, quit_driver):
        LoggerUtils().info("Step 1. Navigating to the Main Page and checking if it is open")
        DriverUtils.navigate(ConfigManager.get_config_data()["url"])
        main_page = MainPage()
        main_page.wait_until_page_is_open()
        assert main_page.is_open(), "It's not Main Page as the unique element is not found"

        LoggerUtils().info("Step 2. Clicking on the Alerts Frame and Windows button. "
                           "Then clicking the Browser Windows Button on the panel. "
                           "Checking if the Browser Windows Page is open")
        main_page.click_alerts_frame_and_windows_button()
        alerts_frame_and_windows_page = AlertsFrameAndWindowsPage()
        alerts_frame_and_windows_page.panel_form.click_browser_windows_button()
        browser_windows_page = BrowserWindowsPage()
        assert browser_windows_page.is_open(), "It's not Browser Windows Page as the unique element is not found"

        LoggerUtils().info("Step 3. Clicking on the New Tab button and checking if the new tab is open")
        initial_tab = DriverUtils.get_tab_id()
        browser_windows_page.click_new_tab_button()
        DriverUtils.switch_to_new_tab(initial_tab)
        new_tab_page = NewTabPage()
        assert new_tab_page.is_open(), "It's not New Tab Page as the unique element is not found"

        LoggerUtils().info("Step 4. Closing the New Tab Page. "
                           + "Checking if the Browser Windows Page is open")
        DriverUtils.close_tab()
        DriverUtils.switch_to_initial_tab(initial_tab)
        assert browser_windows_page.is_open(), "It's not Browser Windows Page as the unique element is not found"

        LoggerUtils().info("Step 5. Clicking the Elements Button on the panel and clicking the Links Button. "
                           "Checking if the Links Page is open")
        browser_windows_page.panel_form.click_elements_button()
        browser_windows_page.panel_form.click_links_button()
        links_page = LinksPage()
        assert links_page.is_open(), "It's not Links Page as the unique element is not found"

        LoggerUtils().info("Step 6. Clicking the Home Link and checking if the Home Page is open")
        initial_tab = DriverUtils.get_tab_id()
        links_page.click_link_to_home_page()
        DriverUtils.switch_to_new_tab(initial_tab)
        assert main_page.is_open(), "It's not Main Page as the unique element is not found"

        LoggerUtils().info("Step 7. Switching to the Links Page and checking if the Links Page is open")
        DriverUtils.switch_to_initial_tab(initial_tab)
        assert links_page.is_open(), "It's not Links Page as the unique element is not found"


class TestSliders:
    def test_sliders_on_the_sliders_and_progress_bar_pages(self, maximize_window, quit_driver):
        LoggerUtils().info("Step 1. Navigating to the Main Page and checking if it is open")
        DriverUtils.navigate(ConfigManager.get_config_data()["url"])
        main_page = MainPage()
        main_page.wait_until_page_is_open()
        assert main_page.is_open(), "It's not Main Page as the unique element is not found"

        LoggerUtils().info("Step 2. Clicking on the Widgets Button and clicking on the Slider Button on the panel. "
                           "Checking if the Slider Page is open")
        main_page.click_widgets_button()
        widgets_page = WidgetsPage()
        widgets_page.panel_form.click_slider_button_with_js()
        slider_page = SliderPage()
        assert slider_page.is_open(), "It's not Slider Page as the unique element is not found"

        LoggerUtils().info("Step 3. Set the Slider to a valid randomly generated value. "
                           "Checking if the value on the page near the slider equals to the set value")
        random_int = RandomUtils.generate_random_int()
        slider_page.click_slider()
        slider_page.wait_until_slider_label_text_is_visible()
        slider_page.set_slider_value(random_int)
        assert slider_page.get_value_from_slider_value_field() == slider_page.get_slider_value(), \
            "The slider's value doesn't equal to the slider's label's value"

        LoggerUtils().info("Step 4. Clicking the Progress Bar Button. Checking if the Progress Bar Page is open")
        slider_page.panel_form.click_progress_bar_button_with_js()
        progress_bar_page = ProgressBarPage()
        assert progress_bar_page.is_open(), "It's not Progress Bar Page as the unique element is not found"

        LoggerUtils().info("Step 5. Clicking on the Start Button.")
        progress_bar_page.click_start_button()

        LoggerUtils().info("Step 6. Clicking on the Stop Button when the value equals to the passed age value. "
                           "Checking if the value on the progress bar equals to the passed age value.")
        if progress_bar_page.wait_until_progress_bar_with_age_value_appears_more_often():
            progress_bar_page.click_stop_button()
        current_value_of_progress_bar = int(progress_bar_page.get_progress_bar_value())
        assert current_value_of_progress_bar - ConfigManager.get_test_data()["progress_bar_possible_range"] \
               <= current_value_of_progress_bar <= current_value_of_progress_bar + \
               ConfigManager.get_test_data()["progress_bar_possible_range"],\
               "The current value on the progress bar doesn't equal to the passed age value"


class TestDatePicker:
    def test_date_picker_on_the_date_picker_page(self, maximize_window, quit_driver):
        LoggerUtils().info("Step 1. Navigating to the Main Page and checking if it is open")
        DriverUtils.navigate(ConfigManager.get_config_data()["url"])
        main_page = MainPage()
        main_page.wait_until_page_is_open()
        assert main_page.is_open(), "It's not Main Page as the unique element is not found"

        LoggerUtils().info("Step 2. Clicking the Widgets Button and then Date Picker Button. "
                           "Checking if the Date Picker Page is open and if the values of Select Date and "
                           "Date And Time fields are equal to current date and time")
        main_page.click_widgets_button()
        widgets_page = WidgetsPage()
        widgets_page.panel_form.click_date_picker_button_with_js()
        date_picker_page = DatePickerPage()
        assert date_picker_page.is_open(), "It's not Date Picker Page as the unique element is not found"
        assert date_picker_page.get_date_from_date_field() == \
               DateUtils.get_current_date_time(ConfigManager.get_test_data()["date_format"]), \
               "The date in the Date Field doesn't equal to the current date"
        assert date_picker_page.get_date_time_from_date_and_time_field() == \
               DateUtils.get_current_date_time(ConfigManager.get_test_data()["date_time_format"]),\
               "The date and time in the Date and Time Field don't equal to the current date and time"

        LoggerUtils().info("Step 3. Picking date in a Date Picker. "
                           "Checking if the value has changed")
        date_picker_page.click_date_field()
        date_picker_page.click_month_selector()
        date_picker_page.choose_month()
        date_picker_page.select_year_that_has_target_date()
        selected_month_date_year = date_picker_page.get_selected_month_date_year()
        date_picker_page.choose_date()
        assert date_picker_page.get_date_from_date_field() == selected_month_date_year,\
               "The selected date doesn't equal to the one set earlier"


class TestFiles:
    def test_uploading_and_downloading_files(self, maximize_window, quit_driver):
        LoggerUtils().info("Step 1. Navigating to the Main Page and checking if it is open")
        DriverUtils.navigate(ConfigManager.get_config_data()["url"])
        main_page = MainPage()
        main_page.wait_until_page_is_open()
        assert main_page.is_open(), "It's not Main Page as the unique element is not found"

        LoggerUtils().info("Step 2. Clicking the Elements Button and then the Upload and Download Button. "
                           "Checking if the Upload and Download Page is open")
        main_page.click_elements_button()
        elements_page = ElementsPage()
        elements_page.panel_form.click_upload_and_download_button_with_js()
        upload_and_download_page = UploadAndDownloadPage()
        assert upload_and_download_page.is_open(), \
            "It's not Upload and Download Page as the unique element is not found"

        LoggerUtils().info("Step 3. Clicking the Download Button and waiting for the file to download. "
                           "Checking if the file is downloaded successfully")
        upload_and_download_page.click_download_button()
        FileUtils.check_if_file_is_downloaded(
            ConfigManager.get_config_data()["default_directory"], ConfigManager.get_test_data()["file"])
        assert FileUtils.check_if_directory_is_empty(ConfigManager.get_config_data()["default_directory"]),\
            "The file is not downloaded as the folder is empty"

        LoggerUtils().info("Step 4. Uploading the previously downloaded file. "
                           "Checking if the file name is displayed")
        upload_and_download_page.send_file_path_to_choose_file_field()
        assert ConfigManager.get_test_data()["file"] in upload_and_download_page.get_text_from_uploaded_path(), \
            "The file name hasn't appeared on the page"
