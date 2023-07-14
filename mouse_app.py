import keyboard
import time
from helper_classes.virtual_keyboard_class import VirtualKeyboard
from controller.mouse_controller_class import MouseController
import pyglet
from pyglet import shapes, clock
from Config import Config

# mouse controller class
# controlls mouse movement and mouse buttons
mouse_controller = MouseController()
window = pyglet.window.Window(Config.KEYBOARD_WIDTH, Config.KEYBOARD_HEIGHT)


@window.event
def on_draw():
    window.clear()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.Q:
        pyglet.exit()


clock.schedule_interval(mouse_controller.check_for_movement, 0.0001)
clock.schedule_interval(mouse_controller.check_for_left_click_triggered, 0.001)
clock.schedule_interval(mouse_controller.check_for_right_click_triggered,
                        0.001)
clock.schedule_interval(mouse_controller.check_for_keyboard_triggered,
                        0.001, window)

pyglet.app.run()
