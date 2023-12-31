from helper_classes.virtual_keyboard_class import VirtualKeyboard
from controller.mouse_controller_class import MouseController
import pyglet
import keyboard
from pyglet import clock
from Config import Config

# mouse controller class
# controlls mouse movement and mouse buttons
virtual_keyboard = VirtualKeyboard()
mouse_controller = MouseController(virtual_keyboard)
window = pyglet.window.Window(Config.KEYBOARD_WIDTH, Config.KEYBOARD_HEIGHT)


@window.event
def on_draw():
    window.clear()
    virtual_keyboard.draw()


@window.event
def on_mouse_motion(x, y, dx, dy):
    mouse_controller.mouse_x = x
    mouse_controller.mouse_y = y


@window.event
def on_mouse_enter(x, y):
    mouse_controller.isCurrentlyUsingKeyboard = True


@window.event
def on_mouse_leave(x, y):
    mouse_controller.isCurrentlyUsingKeyboard = False

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.Q:
        window.close()
       # mouse_controller.disconnet()
    elif symbol == pyglet.window.key.C:
        mouse_controller.show_capabilities()

def check_for_key_press(dt):
    # exit application
    if keyboard.is_pressed('q'):
        window.close()
    
    # show all available / missing capabilities
    if keyboard.is_pressed('c'):
        mouse_controller.show_capabilities()


clock.schedule_interval(mouse_controller.check_for_movement, 0.00001)
clock.schedule_interval(mouse_controller.check_for_left_click_triggered, 0.001)
clock.schedule_interval(mouse_controller.check_for_right_click_triggered,
                        0.001)
clock.schedule_interval(mouse_controller.check_for_keyboard_triggered,
                        0.001, window)
clock.schedule_interval(check_for_key_press, 0.001)

virtual_keyboard.init_keyboard()

pyglet.app.run()
