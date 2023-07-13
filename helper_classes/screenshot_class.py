import pyautogui
import uuid
import keyboard

from PIL import Image
from Config import Config
from pyautogui import press


class ScreenshotFeature():

    def __init__(self):
        self.screenshot:Image = None

    def take_and_save_screenshot(self):
        save_path = Config.SCREENSHOT_FOLDER_PATH + f"screenshot_{uuid.uuid4}.png"
        self.screenshot = pyautogui.screenshot(save_path)

    def take_screenshot(self):
        press("printscreen")