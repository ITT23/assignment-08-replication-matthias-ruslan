# used to store magic numbers and strings

class Config:
    # error messages
    MISSING_ACCELEROMETER_EXCEPTION = "sensor has no accelerometer capability"
    MISSING_BTN_1_EXCEPTION = "sensor has no button 1 capability"
    MISSING_BTN_2_EXCEPTION = "sensor has no button 2 capability"

    # magic numbers
    MOUSE_MOVEMENT_SCALING_POSITIV = 10  # multiplication of the x and y accelerometer values
    MOUSE_MOVEMENT_SCALING_NEGATIVE = -10  # multiplication of the x and y accelerometer values
    MOUSE_MOVEMENT_THRESHOLD_POSITIV = 0.3 # value that must be exceeded in order for a mouse movement to be initiated.
    MOUSE_MOVEMENT_THRESHOLD_NEGATIVE = -0.3 # value that must be fallen below in order for a mouse movement to be initiated.