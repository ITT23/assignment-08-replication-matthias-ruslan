import keyboard
import time

from classes.mouse_class import Mouse

mouse_controller = Mouse()

while(True):
    mouse_controller.move()
    if keyboard.is_pressed('q'):
        mouse_controller.disconnet()
        break
    #time.sleep(0.1)