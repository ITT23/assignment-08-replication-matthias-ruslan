import pyautogui
from PIL import Image

class ScreenshotFeature():

    def __init__(self):
        self.screenshot:Image = None

    def take_screenshot(self):
        self.screenshot = pyautogui.screenshot('my_screenshot.png')