import pyglet.graphics
from Config import Config
from data.keyboard_buttons_dict import rows
from pyglet import shapes
from pynput.keyboard import Controller

keyboard = Controller()


class VirtualKeyboard:

    def __init__(self):
        self.buttons = rows
        self.key_batch = None
        self.key_shapes = []
        self.caps_on = False

    # maps over keyboard definitions and displays all creates array with
    # all buttons to draw
    def init_keyboard(self):
        self.key_batch = pyglet.graphics.Batch()
        for i in range(0, len(rows)):

            symbol_key = 'shift_symbol' if self.caps_on else 'symbol'
            input_key = 'shift_input' if self.caps_on else 'input'
            currentRow = rows[i]

            row_length = currentRow['row_length']
            row_position = currentRow['row_position']
            keys = currentRow['keys']

            pos_counter = 0
            for key in keys:
                key_width = keys[key]['width']
                key_height = keys[key]['height']
                x_pos = pos_counter * (Config.KEYBOARD_WIDTH / row_length)
                pos_counter += keys[key]['space']
                y_pos = (Config.KEYBOARD_HEIGHT - (
                            key_height * row_position)) - row_position
                key_shape = shapes.Rectangle(int(x_pos), y_pos, key_width,
                                             key_height,
                                             color=(191, 191, 191, 255),
                                             batch=self.key_batch)
                key_text = pyglet.text.Label(keys[key][symbol_key],
                                             font_size=12,
                                             color=(0, 0, 0, 255),
                                             batch=self.key_batch)
                text_x = x_pos + (key_width - key_text.content_width) // 2
                text_y = y_pos + (key_height - key_text.content_height) // 2
                key_text.x = text_x
                key_text.y = text_y
                self.key_shapes.append(
                    {"shape": key_shape, "label": key_text, "x": int(x_pos),
                     "y": y_pos,
                     'width': key_width, 'height': key_height,
                     'input': keys[key][input_key],
                     'symbol': keys[key][symbol_key]})

    # Checks which button was clicked
    def check_key_input(self, x, y):
        for i in range(0, len(self.key_shapes)):
            key = self.key_shapes[i]
            if key['x'] <= x <= key['x'] + key['width']:
                if key['y'] <= y <= key['y'] + key['height']:
                    keyboard.press(key['input'])
                    if key['symbol'] == 'CapsLk':
                        self.caps_on = not self.caps_on
                        self.key_batch = None
                        self.key_shapes = []
                        self.init_keyboard()

    def draw(self):
        self.key_batch.draw()
