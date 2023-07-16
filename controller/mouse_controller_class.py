# mouse controller

# package to controll mouse
import time

import pyautogui
# stores strings an magic numbers
from Config import Config
# DIPPID functionality
from DIPPID import SensorUDP

# gesture recognizer class
from helper_classes.recognizer_class import Recognizer
# screenshot feature class
from helper_classes.screenshot_class import ScreenshotFeature
# arrow navigation feature
from helper_classes.arrow_navigation_class import ArrowNavigation
# application launcher feature
from helper_classes.applicationsLauncher_class import ApplicationLauncher

# enums
from enums.gestures_enum import \
    Gesture  # for the one-dollar-recognizer gestures
from enums.arrow_navigation_enum import ArrowKeys  # up, down, left and right

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)


class MouseController():

    def __init__(self, virtual_keyboard):
        # values ​​that are added to / subtracted from the current position of the x / y coordinates based on the accelerometer data
        self.blit_pos_x: float = 0.0
        self.blit_pos_y: float = 0.0
        # left and right mouse button
        # 0 = not pressed / released; 1 = pressed
        self.left_click: int = 0
        self.right_click: int = 0
        self.mouse_down_left: bool = False
        # value by which to multiply the x and y blit values
        self.movement_scaler_neg = Config.MOUSE_MOVEMENT_SCALING
        # one-dollar-gesture-recognizer
        self.gesture_recoginzer = Recognizer()
        # class for the screenshot functionalities
        self.screenshot_feature = ScreenshotFeature()
        # class for the arrow navigation functionalities
        self.arrow_nav_feature = ArrowNavigation()
        # class for the application launcher functionalities
        self.application_launcher_feature = ApplicationLauncher()
        # class for they keyboard functionalities
        self.virtual_keyboard = virtual_keyboard
        # if keyboard window is visible
        self.windowVisibility = True
        # user is currently inside the keyboard window
        self.isCurrentlyUsingKeyboard = False
        # mouse positions inside the keyboard window
        self.mouse_x = 0
        self.mouse_y = 0

    # move cursor based on the accelerometer data
    # to move a certain threshold needs to be passed
    # cursor speed is to be increased continuously up to a certain value during movement and reset again when stationary.
    # If button 4 is pressed, this method also uses the accelerometer data to determine which arrow navigation should take place (up, down, left or right arrow key).
    def check_for_movement(self, dx):
        if sensor.has_capability('accelerometer'):
            # get DIPPID accelerometer data
            self.blit_pos_x = float(sensor.get_value('accelerometer')['x'])
            self.blit_pos_y = float(sensor.get_value('accelerometer')['y'])

            # x accelerometer value needs to exceed a threshold
            if self.blit_pos_x > Config.MOUSE_MOVEMENT_THRESHOLD_POSITIV or self.blit_pos_x < Config.MOUSE_MOVEMENT_THRESHOLD_NEGATIVE:  # threshold +/- 0.3
                self.blit_pos_x *= self.movement_scaler_neg  # scale value -> display width * 0.005

                # check in the further process whether button 4 is pressed. If yes, inform whether it is an left or right arrow navigation depending on the x blit value.
                if self.blit_pos_x < 0:
                    self.check_for_arrow_navigation_triggered(ArrowKeys.LEFT)
                else:
                    self.check_for_arrow_navigation_triggered(ArrowKeys.RIGHT)
            else:
                # mouse cursor should not move because threshold was not passed
                self.blit_pos_x = 0.0

            # y accelerometer value needs to exceed a threshold
            if self.blit_pos_y > Config.MOUSE_MOVEMENT_THRESHOLD_POSITIV or self.blit_pos_y < Config.MOUSE_MOVEMENT_THRESHOLD_NEGATIVE:  # threshold +/- 0.3
                self.blit_pos_y *= self.movement_scaler_neg  # display width * 0.005

                # check in the further process whether button 4 is pressed. If yes, inform whether it is an up or down arrow navigation depending on the y blit value.
                if self.blit_pos_y < 0:
                    self.check_for_arrow_navigation_triggered(ArrowKeys.UP)
                else:
                    self.check_for_arrow_navigation_triggered(ArrowKeys.DOWN)
            else:
                # mouse cursor should not move because threshold was not passed
                self.blit_pos_y = 0.0

            # move cursor depending on the blit x / y blit values
            pyautogui.moveRel(self.blit_pos_x, self.blit_pos_y)
            # adjust cursor speed
            self.adjust_cursor_speed()

    # cursor speed is to be increased continuously up to a certain value during movement and reset again when stationary.
    def adjust_cursor_speed(self):
        # if cursor hasn't moved
        if not (
                self.blit_pos_x > Config.MOUSE_MOVEMENT_THRESHOLD_POSITIV or self.blit_pos_x < Config.MOUSE_MOVEMENT_THRESHOLD_NEGATIVE) and not \
                (
                        self.blit_pos_y > Config.MOUSE_MOVEMENT_THRESHOLD_POSITIV or self.blit_pos_y < Config.MOUSE_MOVEMENT_THRESHOLD_NEGATIVE):
            # reset scaler
            self.movement_scaler_neg = Config.MOUSE_MOVEMENT_SCALING
        else:
            # increase scaler
            if self.movement_scaler_neg > Config.MOUSE_MOVEMENT_SCALING_THRESHOLD:  # scaler limit is -50
                self.movement_scaler_neg -= 1

            # check if button 3 is pressed. If yes, initiate gesture recognition
            # With gesture recognition, the x / y coordinates are recorded.
            # Since you don't want this to happen while the cursor is still, this is the best place for the check process.
            self.check_for_gesture_feature_triggered()

    # trigger left mouse button if DIPPID button 1 was clicked
    def check_for_left_click_triggered(self, dx):
        if sensor.has_capability('button_1'):
            self.left_click = sensor.get_value('button_1')
            if self.left_click == 1:
                if self.isCurrentlyUsingKeyboard and self.windowVisibility:
                    self.virtual_keyboard.check_key_input(self.mouse_x,
                                                          self.mouse_y)
                else:
                    if self.mouse_down_left is False:
                        pyautogui.mouseDown(button='left')
                        self.mouse_down_left = True
                self.check_for_copy_paste_triggered()
            elif self.mouse_down_left:
                pyautogui.mouseUp(button='left')
                self.mouse_down_left = False

    # trigger right mouse button if DIPPID button 2 was clicked
    def check_for_right_click_triggered(self, dx):
        if sensor.has_capability('button_2'):
            self.right_click = sensor.get_value('button_2')

            if self.right_click == 1 and self.left_click == 0:
                pyautogui.click(button="right")

    # copy/paste feature
    def check_for_copy_paste_triggered(self):
        if sensor.has_capability('button_2') and sensor.has_capability(
                'button_3'):
            # COPY: button 1 + button 2 (holding left and right mouse button)
            if self.right_click == 1:
                pyautogui.hotkey('ctrl', 'c')
            # PASTE: button 1 + button 3
            elif sensor.get_value('button_3') == 1:
                pyautogui.hotkey('ctrl', 'v')
                print(Config.PASTE_MESSAGE)

    # keyboard visibility toggle
    def check_for_keyboard_triggered(self, dx, window):
        if sensor.has_capability('button_3') and sensor.has_capability(
                'button_4'):
            button3_click = sensor.get_value('button_3')
            button4_click = sensor.get_value('button_4')
            if button3_click and button4_click:
                window.set_visible(not self.windowVisibility)
                self.windowVisibility = not self.windowVisibility

    # arrow navigation using mouse cursor
    def check_for_arrow_navigation_triggered(self,
                                             nav_direction: ArrowNavigation):  # passing the arrow navigation direction when moving the cursor
        # arrow navigation only if "button_4" capability is present
        if sensor.has_capability('button_4'):
            # and button 4 is pressed/held.
            if sensor.get_value('button_4') == 1:
                if nav_direction is ArrowKeys.UP:
                    self.arrow_nav_feature.up()
                elif nav_direction is ArrowKeys.DOWN:
                    self.arrow_nav_feature.down()
                elif nav_direction is ArrowKeys.LEFT:
                    self.arrow_nav_feature.left()
                elif nav_direction is ArrowKeys.RIGHT:
                    self.arrow_nav_feature.right()

    # collects the x and y coordinates of the gesture drawing
    def check_for_gesture_feature_triggered(self):
        # gesture recognition feature only if "button_3" capability is present
        if sensor.has_capability('button_3'):
            # and button 3 is pressed/held.
            if sensor.get_value('button_3') == 1:
                # Get the current mouse position
                current_x, current_y = pyautogui.position()
                current_x += self.blit_pos_x
                current_y += self.blit_pos_y
                # save point in the recognizer
                self.gesture_recoginzer.add_point(int(current_x),
                                                  int(current_y))

            # if button 3 released -> start the gesture recogniton process
            else:
                # avoid unnecessary recognition process
                if len(self.gesture_recoginzer.input_points) > 10:
                    self.init_gesture_feature()

    # features based on the recognized gesture
    def init_gesture_feature(self):
        # result of the gesture recognition
        self.gesture_recoginzer.recognize()

        matched_template = self.gesture_recoginzer.get_matching_template()

        if not (
        self.application_launcher_feature.init_application(matched_template)):
            # SCREENSHOT FEATURE
            # gesture "v" -> take screenshot and save it in the screenshot folder
            if matched_template == Gesture.V.value:
                self.screenshot_feature.take_and_save_screenshot()
                print(Config.SCREENSHOOT_MESSAGE_V)

                # gesture "check" -> take the screenshot and save it to the clipboard
            elif matched_template == Gesture.CHECK.value:
                self.screenshot_feature.take_screenshot()
                print(Config.SCREENSHOOT_MESSAGE_CHECK)

        # reset recognizer
        self.gesture_recoginzer.reset_recognizer()

    # disconnet from sensor
    def disconnet(self):
        sensor.disconnect()

    # show available / missing capabilities
    def show_capabilities(self):
        if not sensor.has_capability('accelerometer'):
            print(Config.MISSING_ACCELEROMETER_EXCEPTION)
        elif not sensor.has_capability('button_1'):
            print(Config.MISSING_BTN_1_EXCEPTION)
        elif not sensor.has_capability('button_2'):
            print(Config.MISSING_BTN_2_EXCEPTION)
        elif not sensor.has_capability('button_3'):
            print(Config.MISSING_BTN_3_EXCEPTION)
        elif not sensor.has_capability('button_4'):
            print(Config.MISSING_BTN_4_EXCEPTION)
        else:
            print(Config.NO_MISSING_CAPABILITIES_MESSAGE)