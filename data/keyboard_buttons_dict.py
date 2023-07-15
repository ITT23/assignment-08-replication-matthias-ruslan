import math
from Config import Config

keyboard_row_1: dict = {
    'row_length': 12,
    'row_position': 1,
    'keys': {'key_1': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/4), 'space': 1, 'symbol': '1', 'input': '1'},
             'key_2': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/4), 'space': 1, 'symbol': '2', 'input': '2'}}
}

rows = [keyboard_row_1]
