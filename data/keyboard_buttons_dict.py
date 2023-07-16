import math
from Config import Config
from pynput.keyboard import Key

# Row Definitions for the Keyboard Layout

keyboard_row_1: dict = {
    'row_length': 12,
    'row_position': 1,
    'keys': {'key_1': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '1', 'input': '1', 'shift_symbol': '!', 'shift_input': '!'},
             'key_2': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '2', 'input': '2', 'shift_symbol': '"', 'shift_input': '"'},
             'key_3': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '3', 'input': '3', 'shift_symbol': '§', 'shift_input': '§'},
             'key_4': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '4', 'input': '4', 'shift_symbol': '$', 'shift_input': '$'},
             'key_5': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '5', 'input': '5', 'shift_symbol': '%', 'shift_input': '%'},
             'key_6': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '6', 'input': '6', 'shift_symbol': '&', 'shift_input': '&'},
             'key_7': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '7', 'input': '7', 'shift_symbol': '/', 'shift_input': '/'},
             'key_8': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '8', 'input': '8', 'shift_symbol': '(', 'shift_input': '('},
             'key_9': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '9', 'input': '9', 'shift_symbol': ')', 'shift_input': ')'},
             'key_0': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '0', 'input': '0', 'shift_symbol': '=', 'shift_input': '='},
             'key_backspace': {'width': ((math.floor(Config.KEYBOARD_WIDTH/12))*2)+1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 2, 'symbol': 'backspace', 'input': Key.backspace, 'shift_symbol': 'backspace', 'shift_input': Key.backspace}}
}

keyboard_row_2: dict = {
    'row_length': 12,
    'row_position': 2,
    'keys': {'key_tab': {'width': (math.floor(Config.KEYBOARD_WIDTH/12))*2, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 2, 'symbol': 'Tab', 'input': Key.tab, 'shift_symbol': 'Tab', 'shift_input': Key.tab},
             'key_Q': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'q', 'input': 'q', 'shift_symbol': 'Q', 'shift_input': 'Q'},
             'key_W': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'w', 'input': 'w', 'shift_symbol': 'W', 'shift_input': 'W'},
             'key_E': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'e', 'input': 'e', 'shift_symbol': 'E', 'shift_input': 'E'},
             'key_R': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'r', 'input': 'r', 'shift_symbol': 'R', 'shift_input': 'R'},
             'key_T': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 't', 'input': 't', 'shift_symbol': 'T', 'shift_input': 'T'},
             'key_Z': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'z', 'input': 'z', 'shift_symbol': 'Z', 'shift_input': 'Z'},
             'key_U': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'u', 'input': 'u', 'shift_symbol': 'U', 'shift_input': 'U'},
             'key_I': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'i', 'input': 'i', 'shift_symbol': 'I', 'shift_input': 'I'},
             'key_O': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'o', 'input': 'o', 'shift_symbol': 'O', 'shift_input': 'O'},
             'key_P': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'p', 'input': 'p', 'shift_symbol': 'P', 'shift_input': 'P'}}
}

keyboard_row_3: dict = {
    'row_length': 12,
    'row_position': 3,
    'keys': {'key_CapsLk': {'width': (math.floor(Config.KEYBOARD_WIDTH/12))*2, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 2, 'symbol': 'CapsLk', 'input': Key.caps_lock, 'shift_symbol': 'CapsLk', 'shift_input': Key.caps_lock},
             'key_A': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'a', 'input': 'a', 'shift_symbol': 'A', 'shift_input': 'A'},
             'key_S': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 's', 'input': 's', 'shift_symbol': 'S', 'shift_input': 'S'},
             'key_D': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'd', 'input': 'd', 'shift_symbol': 'D', 'shift_input': 'D'},
             'key_F': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'f', 'input': 'f', 'shift_symbol': 'F', 'shift_input': 'F'},
             'key_G': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'g', 'input': 'g', 'shift_symbol': 'G', 'shift_input': 'G'},
             'key_H': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'h', 'input': 'h', 'shift_symbol': 'H', 'shift_input': 'H'},
             'key_J': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'j', 'input': 'j', 'shift_symbol': 'J', 'shift_input': 'J'},
             'key_K': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'k', 'input': 'k', 'shift_symbol': 'K', 'shift_input': 'K'},
             'key_L': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'l', 'input': 'l', 'shift_symbol': 'L', 'shift_input': 'L'},
             'key_Enter': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'Enter', 'input': Key.enter, 'shift_symbol': 'Enter', 'shift_input': Key.enter}}
}

keyboard_row_4: dict = {
    'row_length': 12,
    'row_position': 4,
    'keys': {'key_shift': {'width': (math.floor(Config.KEYBOARD_WIDTH/12))*2, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 2, 'symbol': 'Shift', 'input': Key.shift, 'shift_symbol': 'Shift', 'shift_input': Key.shift},
             'key_Y': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'y', 'input': 'y', 'shift_symbol': 'Y', 'shift_input': 'Y'},
             'key_X': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'x', 'input': 'x', 'shift_symbol': 'X', 'shift_input': 'X'},
             'key_C': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'c', 'input': 'c', 'shift_symbol': 'C', 'shift_input': 'C'},
             'key_V': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'v', 'input': 'v', 'shift_symbol': 'V', 'shift_input': 'V'},
             'key_B': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'b', 'input': 'b', 'shift_symbol': 'B', 'shift_input': 'B'},
             'key_N': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'n', 'input': 'n', 'shift_symbol': 'N', 'shift_input': 'N'},
             'key_M': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': 'm', 'input': 'm', 'shift_symbol': 'M', 'shift_input': 'M'},
             'key_comma': {'width': math.floor(Config.KEYBOARD_WIDTH/12)-1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': ',', 'input': ',', 'shift_symbol': ';', 'shift_input': ';'},
             'key_point': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '.', 'input': '.', 'shift_symbol': ':', 'shift_input': ':'},
             'key_minus': {'width': math.floor(Config.KEYBOARD_WIDTH/12), 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 1, 'symbol': '-', 'input': '-', 'shift_symbol': '_', 'shift_input': '_'},
             }
}

keyboard_row_5: dict = {
    'row_length': 12,
    'row_position': 5,
    'keys': {'key_ctrl': {'width': (math.floor(Config.KEYBOARD_WIDTH/12))*2, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 2, 'symbol': 'Strg', 'input': Key.ctrl, 'shift_symbol': 'Strg', 'shift_input': Key.ctrl},
             'key_alt': {'width': (math.floor(Config.KEYBOARD_WIDTH/12))*2, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 2, 'symbol': 'Alt', 'input': Key.alt, 'shift_symbol': 'Alt', 'shift_input': Key.alt},
             'key_space': {'width': ((math.floor(Config.KEYBOARD_WIDTH/12))*6)+3, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 6, 'symbol': 'Space', 'input': Key.space, 'shift_symbol': 'Space', 'shift_input': Key.space},
             'key_altGr': {'width': ((math.floor(Config.KEYBOARD_WIDTH/12))*2)+1, 'height': math.floor(Config.KEYBOARD_HEIGHT/5), 'space': 2, 'symbol': 'AltGr', 'input': Key.alt_gr, 'shift_symbol': 'AltGr', 'shift_input': Key.alt_gr},
             }
}

rows = [keyboard_row_1, keyboard_row_2, keyboard_row_3, keyboard_row_4, keyboard_row_5]
