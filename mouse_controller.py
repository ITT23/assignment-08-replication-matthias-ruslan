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
    # exit DIPPID mouse movement
    if keyboard.is_pressed('q'):
        mouse_controller.disconnet()
        break
    #time.sleep(0.1)