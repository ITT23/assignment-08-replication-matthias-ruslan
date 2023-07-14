# used to take screenshots with the "check" and "v" gesture

import pyautogui
import uuid
from PIL import Image
from Config import Config
from pyautogui import press

class ScreenshotFeature():

    def __init__(self):
        self.screenshot:Image = None

    # takes screenshot and saves it in the screenshot folder
    def take_and_save_screenshot(self):
        save_path = Config.SCREENSHOT_FOLDER_PATH + f"screenshot_{uuid.uuid4()}.png"
        self.screenshot = pyautogui.screenshot(save_path)

    # just takes the screenshot (imitates the screenshot buttons "alt + print")
    # screenshot can then be pasted in an editor (like paint editor) 
    def take_screenshot(self):
        press("printscreen")