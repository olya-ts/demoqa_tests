from framework.utils.logger_utils import LoggerUtils
from framework.base_classes.base_element import BaseElement


class Button(BaseElement):
    pass


class Text(BaseElement):
    pass


class DropDownList(BaseElement):
    pass


class Link(BaseElement):
    pass


class ProgressBar(BaseElement):
    pass


class Label(BaseElement):
    pass


class TextField(BaseElement):
    def send_text(self, text: str):
        LoggerUtils().debug("Sending the text '%s' to the element '%s'", text, self._name)
        self._find_element().send_keys(text)


class Slider(BaseElement):
    def set_slider(self, label: Label, new_value: int):
        LoggerUtils().debug("Setting the slider value to '%s'", new_value)
        if new_value > int(label.get_text()):
            while int(label.get_text()) != new_value:
                self.press_right_arrow()
        elif new_value < int(label.get_text()):
            while int(label.get_text()) != new_value:
                self.press_left_arrow()
