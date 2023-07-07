import keyboard

from DIPPID import SensorUDP
from classes.mouse_class import Mouse
from Config import Config

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

mouse_controller = Mouse()

def handle_accelerometer_data(data):
    if(sensor.has_capability('accelerometer')):
        mouse_controller.set_mouse_pos(data['x'], data['y'])
        mouse_controller.move()
    else:
        raise Exception(Config.MISSING_ACCELEROMETER_EXCEPTION)
    
def handle_btn_1_data(data):
    if(sensor.has_capability('button_1')):
        mouse_controller.set_mouse_btn_1_state(data)
        # for testing purposes
        if mouse_controller.left_click == 1:
            print("left mouse button was clicked")
    else:
        raise Exception(Config.MISSING_BTN_1_EXCEPTION)

def handle_btn_2_data(data):
    if(sensor.has_capability('button_2')):
        mouse_controller.set_mouse_btn_2_state(data)
        if mouse_controller.right_click == 1:
            print("right mouse button was clicked")
    else:
        raise Exception(Config.MISSING_BTN_2_EXCEPTION)


sensor.register_callback('accelerometer', handle_accelerometer_data)
sensor.register_callback('button_1', handle_btn_1_data)
sensor.register_callback('button_2', handle_btn_2_data)

while(True):
    if keyboard.is_pressed('q'):
        sensor.disconnect()
        break