import keyboard
from DIPPID import SensorUDP
from classes.mouse_class import Mouse
from Config import Config
import numpy as np
from test_ml.recognizer import main, continous_prediction, \
    check_for_buttonclick

# use UPD (via WiFi) for communication
# PORT = 5700
# sensor = SensorUDP(PORT)

mouse_controller = Mouse()


class Test():

    def __init__(self):
        self.classifier, self.encoder = main()
        self.predictions = []

    def update(self):
        pred = continous_prediction(classifier=self.classifier,
                                    encoder=self.encoder)

        print(pred)


'''
def handle_accelerometer_data(data):
    if sensor.has_capability('accelerometer'):
        l = 1
        #mouse_controller.set_mouse_pos(data['x'], data['y'])
        #mouse_controller.move()
    else:
        raise Exception(Config.MISSING_ACCELEROMETER_EXCEPTION)


def handle_gyroscope_data(data):
    if sensor.has_capability('gyroscope'):
        mouse_controller.set_mouse_pos(data['x'], data['y'])
        mouse_controller.move()

def handle_btn_1_data(data):
    if sensor.has_capability('button_1'):
        mouse_controller.set_mouse_btn_1_state(data)
        # for testing purposes
        if mouse_controller.left_click == 1:
            print("left mouse button was clicked")
    else:
        raise Exception(Config.MISSING_BTN_1_EXCEPTION)


def handle_btn_2_data(data):
    if sensor.has_capability('button_2'):
        mouse_controller.set_mouse_btn_2_state(data)
        if mouse_controller.right_click == 1:
            print("right mouse button was clicked")
    else:
        raise Exception(Config.MISSING_BTN_2_EXCEPTION)


sensor.register_callback('accelerometer', handle_accelerometer_data)
sensor.register_callback('button_1', handle_btn_1_data)
sensor.register_callback('button_2', handle_btn_2_data)
sensor.register_callback('gyroscope', handle_gyroscope_data)
'''

test = Test()
while True:
    test.update()
    if keyboard.is_pressed('q'):
        break
