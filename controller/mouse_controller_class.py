# mouse class

# package to controll mouse
import pyautogui
# stores strings an magic numbers
from Config import Config
# DIPPID functionality 
from DIPPID import SensorUDP

# gesture recognizer class
from helper_classes.recognizer_class import Recognizer
# screenshot feature class
from helper_classes.screenshot_class import ScreenshotFeature
from enums.gestures_enum import Gesture


# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

class MouseController():

    def __init__(self):
        self.blit_pos_x:float = 0.0
        self.blit_pos_y:float = 0.0
        self.left_click:int = 0
        self.right_click:int = 0
        self.movement_scaler_neg = Config.MOUSE_MOVEMENT_SCALING
        self.gesture_recoginzer = Recognizer()
        self.screenshot_feature = ScreenshotFeature()
        

    # get DIPPID accelerometer data and move mouse according to it
    # x/y accelerometer value needs to exceed a threshold
    def check_for_movement(self):
        if sensor.has_capability('accelerometer'):
            self.blit_pos_x = float(sensor.get_value('accelerometer')['x'])
            self.blit_pos_y = float(sensor.get_value('accelerometer')['y'])

            if self.blit_pos_x > Config.MOUSE_MOVEMENT_THRESHOLD_POSITIV or self.blit_pos_x < Config.MOUSE_MOVEMENT_THRESHOLD_NEGATIVE: # threshold +/- 0.3
                self.blit_pos_x *= self.movement_scaler_neg # display width * 0.005
            else:
                self.blit_pos_x = 0.0
            
            if self.blit_pos_y > Config.MOUSE_MOVEMENT_THRESHOLD_POSITIV or self.blit_pos_y < Config.MOUSE_MOVEMENT_THRESHOLD_NEGATIVE: # threshold +/- 0.3
                self.blit_pos_y *= self.movement_scaler_neg # display width * 0.005
            else:
                self.blit_pos_y = 0.0

            pyautogui.moveRel(self.blit_pos_x, self.blit_pos_y)
            self.adjust_cursor_speed()
        else:
            print(Config.MISSING_ACCELEROMETER_EXCEPTION)
    
    def adjust_cursor_speed(self):
        if not (self.blit_pos_x > Config.MOUSE_MOVEMENT_THRESHOLD_POSITIV or self.blit_pos_x < Config.MOUSE_MOVEMENT_THRESHOLD_NEGATIVE) and not \
                (self.blit_pos_y > Config.MOUSE_MOVEMENT_THRESHOLD_POSITIV or self.blit_pos_y < Config.MOUSE_MOVEMENT_THRESHOLD_NEGATIVE):
                self.movement_scaler_neg = Config.MOUSE_MOVEMENT_SCALING
        else:
            if self.movement_scaler_neg > -50:
                self.movement_scaler_neg -= 1
            
            self.check_for_gesture_feature_triggered()
     

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

    def check_for_gesture_feature_triggered(self):
        if sensor.has_capability('button_3'):
            if sensor.get_value('button_3') is 1:
                # Get the current mouse position
                current_x, current_y = pyautogui.position()
                current_x += self.blit_pos_x
                current_y += self.blit_pos_y
                self.gesture_recoginzer.add_point(int(current_x), int(current_y))


            else:
                if len(self.gesture_recoginzer.input_points) is not 0:
                    self.init_gesture_feature()

    def init_gesture_feature(self):
        self.gesture_recoginzer.recognize()

        if self.gesture_recoginzer.get_matching_template() == Gesture.V.value:
            self.screenshot_feature.take_and_save_screenshot()
            
        elif self.gesture_recoginzer.get_matching_template() == Gesture.CHECK.value:
            self.screenshot_feature.take_screenshot()

        self.gesture_recoginzer.reset_recognizer()

    # disconnet from sensor
    def disconnet(self):
        sensor.disconnect()