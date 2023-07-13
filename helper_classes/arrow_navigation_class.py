# class for arrow key navigation using a mouse cursor

from pyautogui import press
from enums.arrow_navigation_enum import ArrowKeys

class ArrowNavigation():

    def __init__(self) -> None:
        pass

    def up(self):
        press(ArrowKeys.UP.value)

    def down(self):
        press(ArrowKeys.DOWN.value)

    def left(self):
        press(ArrowKeys.LEFT.value)

    def right(self):
        press(ArrowKeys.RIGHT.value)