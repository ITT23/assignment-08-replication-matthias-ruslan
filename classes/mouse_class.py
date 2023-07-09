# mouse class

import pyautogui
from Config import Config

class Mouse():

    def __init__(self):
        self.pos_x:float = 0.0
        self.pos_y:float = 0.0
        self.left_click:int = 0
        self.right_click:int = 0

    def set_mouse_pos(self, new_x_pos, new_y_pos):
        self.pos_x = new_x_pos
        self.pos_y = new_y_pos

    def move(self):

        if self.pos_x > 0.3 or self.pos_x < -0.3:
            self.pos_x *= -10
        else:
            self.pos_x = 0.0
        
        if self.pos_y > 0.3 or self.pos_y < -0.3:
            self.pos_y *= 10
        else:
            self.pos_y = 0.0

        pyautogui.moveRel(self.pos_x, self.pos_y) # scaled by 10

    def set_mouse_btn_1_state(self, new_left_btn_state):
        self.left_click = new_left_btn_state
    
    def set_mouse_btn_2_state(self, new_right_btn_state):
        self.right_click = new_right_btn_state
