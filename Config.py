# used to store magic numbers and strings

# display proparties
import tkinter
from os import path

# need to get the display properties
root = tkinter.Tk()


class Config:
    # error messages
    MISSING_ACCELEROMETER_EXCEPTION = "MISSING CAPABILITY: Sensor has no accelerometer capability. Mouse Curso movement and most features doesn't gonna work."
    MISSING_BTN_1_EXCEPTION = "MISSING CAPABILITY: Sensor has no button 1 capability. Left mouse button and some features not gonna work."
    MISSING_BTN_2_EXCEPTION = "MISSING CAPABILITY: Sensor has no button 2 capability. Right mouse button and some features not gonna work."
    MISSING_BTN_3_EXCEPTION = "MISSING CAPABILITY: Sensor has no button 3 capability. Gesture recognition, virtual keyboard and and some other features not gonna work."
    MISSING_BTN_4_EXCEPTION = "MISSING CAPABILITY: Sensor has no button 4 capability. Arrow navigation, virtual keyboard and and some other features not gonna work."
    NO_MISSING_CAPABILITIES_MESSAGE = "All required capabilities are available"
    WRONG_APPLICATION_PATH_EXCEPTION = "Application could not be launched, make sure the path is correct"

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

    # feature messages
    SCREENSHOOT_MESSAGE_V = "Screenshoot was taken and saved in the screenshot folder."
    SCREENSHOOT_MESSAGE_CHECK = "Screenshot was taken and saved in the clipboard"
    COPY_MESSAGE = "Marked text was copied."
    PASTE_MESSAGE = "Text was pasted."
