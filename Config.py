# used to store magic numbers and strings

class Config:
    # error messages
    MISSING_ACCELEROMETER_EXCEPTION = "sensor has no accelerometer capability"
    MISSING_BTN_1_EXCEPTION = "sensor has no button 1 capability"
    MISSING_BTN_2_EXCEPTION = "sensor has no button 2 capability"

    # magic numbers
    MOUSE_MOVEMENT_SCALING = 10  # multiplication of the x and y accelerometer values