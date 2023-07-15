import keyboard

from controller.mouse_controller_class import MouseController

# mouse controller class
# controlls mouse movement and mouse buttons
mouse_controller = MouseController()

while(True):
    # moves the mouse (DIPPID acceleromter)
    mouse_controller.check_for_movement()
    # triggers left mouse button if clicked (DIPPID btn 1)
    mouse_controller.check_for_left_click_triggered()
    # triggers right mouse button if clicked (DIPPID btn 2)
    mouse_controller.check_for_right_click_triggered()

    # exit application
    if keyboard.is_pressed('q'):
        mouse_controller.disconnet()
        break
    # show all available / missing capabilities
    if keyboard.is_pressed('c'):
        mouse_controller.show_capabilities()

