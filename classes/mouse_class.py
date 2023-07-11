# mouse class

# package to controll mouse
import pyautogui
# stores strings an magic numbers
from Config import Config
# DIPPID functionality 
from DIPPID import SensorUDP

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

# Get the screen dimensions
screen_width, screen_height = pyautogui.size()


class Mouse:

    def __init__(self):
        self.pos_x: float = 0.0
        self.pos_y: float = 0.0
        self.left_click: int = 0
        self.right_click: int = 0
        self.min_x = -0.5
        self.max_x = 0.5
        self.max_y = 0.5
        self.min_y = -0.5
        self.max_speed = 20

    # Map the accelerometer values to the screen coordinates
    def map_values(self, acc_value, acc_min, acc_max, screen_min, screen_max):
        return ((acc_value - acc_min) / (acc_max - acc_min)) * (
                    screen_max - screen_min) + screen_min

    # get DIPPID accelerometer data and move mouse according to it
    # x/y accelerometer value needs to exceed a threshold
    def move(self):
        if sensor.has_capability('accelerometer'):
            # get the accelerometer values and map them
            raw_x = float(sensor.get_value('accelerometer')['x'])
            raw_y = float(sensor.get_value('accelerometer')['y'])
            self.pos_x = self.map_values(raw_x, self.min_x, self.max_x, 0, screen_width)
            self.pos_y = self.map_values(raw_y, self.min_y, self.max_y, 0, screen_height)

            # Get the current mouse position
            current_x, current_y = pyautogui.position()

            # Calculate the distance to move the mouse
            delta_x = -(self.pos_x - current_x)
            delta_y = self.pos_y - current_y

            # Calculate the magnitude of the movement
            magnitude = (delta_x ** 2 + delta_y ** 2) ** 0.5

            # Calculate the normalized direction of the movement
            if magnitude > self.max_speed:
                direction_x = delta_x / magnitude
                direction_y = delta_y / magnitude
                delta_x = direction_x * self.max_speed
                delta_y = direction_y * self.max_speed

            # Move the mouse
            pyautogui.move(-delta_x, -delta_y)
        else:
            print(Config.MISSING_ACCELEROMETER_EXCEPTION)

    # trigger left mouse button if DIPPID button 1 was clicked
    def check_for_left_click_triggered(self):
        if sensor.has_capability('button_1'):
            self.left_click = sensor.get_value('button_1')
            if self.left_click == 1:
                pyautogui.click(button="left")
        else:
            print(Config.MISSING_BTN_1_EXCEPTION)

    # trigger right mouse button if DIPPID button 2 was clicked
    def check_for_right_click_triggered(self):
        if sensor.has_capability('button_2'):
            self.left_click = sensor.get_value('button_2')
            if self.left_click == 1:
                pyautogui.click(button="right")
        else:
            print(Config.MISSING_BTN_2_EXCEPTION)

    def check_for_speed_down_triggered(self):
        if sensor.has_capability('button_3'):
            button = sensor.get_value('button_3')
            if button == 1:
                self.max_speed -= 1

    def check_for_speed_up_triggered(self):
        if sensor.has_capability('button_4'):
            button = sensor.get_value('button_4')
            if button == 1:
                self.max_speed += 1

    # disconnect from sensor
    def disconnect(self):
        sensor.disconnect()
