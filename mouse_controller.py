import keyboard
import time

from classes.mouse_class import Mouse

# mouse controller class
# controlls mouse movement and mouse buttons
mouse_controller = Mouse()

while(True):
    # moves the mouse (DIPPID acceleromter)
    mouse_controller.move()
    # triggers left mouse button if clicked (DIPPID btn 1)
    mouse_controller.check_for_left_click_triggered()
    # triggers right mouse button if clicked (DIPPID btn 2)
    mouse_controller.check_for_right_click_triggered()
    mouse_controller.check_for_speed_down_triggered()
    mouse_controller.check_for_speed_up_triggered()
    # exit DIPPID mouse movement
    if keyboard.is_pressed('q'):
        mouse_controller.disconnect()
        break
    #time.sleep(0.1)