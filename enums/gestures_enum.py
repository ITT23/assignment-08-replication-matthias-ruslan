# enum class for the recognizable one-dollar-recognizer gestures

from enum import Enum

class Gesture(Enum):

    CHECK = "check"
    TRIANGLE = "triangle"
    X = "x"
    RECTANGLE = "rectangle"
    CIRCLE = "circle"
    CARET = "caret"
    ARROW = "arrow"
    LEFT_SQUARE_BRACKET = "left square bracket"
    RIGHT_SQUARE_BRACKET = "right square bracket"
    V = "v"
    DELETE = "delete" 
    RIGHT_CURLY_BRACE = "right curly brace"
    STAR = "star"
    PIGTAIL = "pigtail"