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

class Mouse():

    def __init__(self):
        self.pos_x:float = 0.0
        self.pos_y:float = 0.0
        self.left_click:int = 0
        self.right_click:int = 0

    # get DIPPID accelerometer data and move mouse according to it
    # x/y accelerometer value needs to exceed a threshold
    def move(self):
        if sensor.has_capability('accelerometer'):
            self.pos_x = float(sensor.get_value('accelerometer')['x'])
            self.pos_y = float(sensor.get_value('accelerometer')['y'])

            if self.pos_x > Config.MOUSE_MOVEMENT_THRESHOLD_POSITIV or self.pos_x < Config.MOUSE_MOVEMENT_THRESHOLD_NEGATIVE: # threshold +/- 10
                self.pos_x *= Config.MOUSE_MOVEMENT_SCALING_NEGATIVE # -10
            else:
                self.pos_x = 0.0
            
            if self.pos_y > Config.MOUSE_MOVEMENT_THRESHOLD_POSITIV or self.pos_y < Config.MOUSE_MOVEMENT_THRESHOLD_NEGATIVE:
                self.pos_y *= Config.MOUSE_MOVEMENT_SCALING_POSITIV # 10
            else:
                self.pos_y = 0.0

            pyautogui.moveRel(self.pos_x, self.pos_y)
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

    # disconnet from sensor
    def disconnet(self):
        sensor.disconnect()
