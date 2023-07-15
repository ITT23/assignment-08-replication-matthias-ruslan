import pyglet.graphics
from Config import Config
from data.keyboard_buttons_dict import rows
from pyglet import shapes
from pynput.keyboard import Key, Controller

keyboard = Controller()


class VirtualKeyboard:

    def __init__(self):
        self.buttons = rows
        self.key_batch = pyglet.graphics.Batch()
        self.key_shapes = []

    def init_keyboard(self):
        for i in range(0, len(rows)):
            currentRow = rows[i]

            row_length = currentRow['row_length']
            row_position = currentRow['row_position']
            keys = currentRow['keys']

            pos_counter = 0
            for key in keys:
                key_width = keys[key]['width']
                key_height = keys[key]['height']
                x_pos = pos_counter * (keys[key]['space'] * (
                        Config.KEYBOARD_WIDTH / row_length))
                pos_counter += keys[key]['space']
                y_pos = Config.KEYBOARD_HEIGHT - (key_height * row_position)
                key_shape = shapes.Rectangle(int(x_pos), y_pos, key_width,
                                             key_height,
                                             color=(191, 191, 191, 255), batch=self.key_batch)
                self.key_shapes.append(
                    {"shape": key_shape, "x": int(x_pos), "y": y_pos,
                     'width': key_width, 'height': key_height,
                     'input': keys[key]['input']})
                print("yyeye")

    def check_key_input(self, x, y):
        print("check")
        for i in range(0, len(self.key_shapes)):
            key = self.key_shapes[i]
            if key['x'] <= x <= key['x'] + key['width']:
                if key['y'] <= y <= key['y'] + key['height']:
                    print('press')
                    keyboard.press(key['input'])

    def draw(self):
        self.key_batch.draw()
        # self.key_batch.draw()
