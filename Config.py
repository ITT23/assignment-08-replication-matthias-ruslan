# used to store magic numbers and strings

# display proparties
import tkinter
from os import path

# need to get the display properties
root = tkinter.Tk()


class Config:
    # error messages
    MISSING_ACCELEROMETER_EXCEPTION = "sensor has no accelerometer capability"
    MISSING_BTN_1_EXCEPTION = "sensor has no button 1 capability"
    MISSING_BTN_2_EXCEPTION = "sensor has no button 2 capability"

    # Display size
    DISPLAY_HEIGHT = root.winfo_screenheight()
    DISPLAY_WIDHT = root.winfo_screenwidth()

    # magic numbers
    MOUSE_MOVEMENT_SCALING = -1 * int(
        DISPLAY_WIDHT * 0.005)  # multiplication of the x and y accelerometer values based on the screen size
    MOUSE_MOVEMENT_SCALING_THRESHOLD = -50
    MOUSE_MOVEMENT_THRESHOLD_POSITIV = 0.3  # value that must be exceeded in order for a mouse movement to be initiated.
    MOUSE_MOVEMENT_THRESHOLD_NEGATIVE = -0.3  # value that must be fallen below in order for a mouse movement to be initiated.

    # path for the folder the screenshots are saved at
    SCREENSHOT_FOLDER_PATH = path.join(path.dirname(__file__), "screenshots\\")

    # path for the application paths
    APPLICATIONS_PATH = path.join(path.dirname(__file__), "applications.txt")
    
    # Keyboard sizing
    KEYBOARD_WIDTH = 800
    KEYBOARD_HEIGHT = 400
    
    # Optional creation mode
    CREATION_MODE = False
    NEW_CREATED_GESTURE_NAME = 'N'
    
