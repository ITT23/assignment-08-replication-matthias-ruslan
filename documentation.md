# Extending/Implementing the interaction technique described in the paper "Mobile Phones as Pointing Devices" with DIPPID
Paper by Ballagas et al. [1]

## Team 

### **Matthias Dobiosz** and **Ruslan Asabidi**

![team](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/0329aa88-5d46-4671-8be0-c8b50baf64d0)


## The Paper

Ballagas et al. [1] developed two complementary camera-based interaction techniques called point & shoot based on optical sensing and sweep based on optical-flow detection. Both techniques can be used for pointing, for example, to control a cursor on a large display. Point & shoot is used for absolute cursor positioning, while sweep realizes relative cursor movement.

### Sweep

![sweep](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/e0ddd98e-1bce-4ae2-8a8a-45ad83728a85)

### Point & Shoot

![point_shoot](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/7dc57d3c-9022-4aab-a70e-6432da6047b4)

## Our Motivation

We were captivated by the concept of utilizing a smartphone as a mouse controller, particularly due to the intriguing prospect of implementing control through DIPPID. The study conducted by Ballagas et al. [1] in 2005 showcased the early stages of this interaction technique, albeit with limited options at the time. In order to carry out the study, an external and cumbersome accelerometer had to be attached.

![handy](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/5aa2de5c-2158-4406-9f91-f85e31bb9d62)

Nowadays, even smartphones in the lower price range come equipped with at least one built-in accelerometer. Moreover, there are additional sensors that provide data on gyroscope and angles, among other things. The DIPPID functionality utilized in this course proves to be highly suitable for expanding upon and implementing the approach outlined in the paper. On one hand, the DIPPID app facilitates effortless acquisition and processing of data from various sensors. On the other hand, the inclusion of four buttons enables mouse button control and the incorporation of practical features related to mouse manipulation.

## Our Goal

Our objective consisted of two phases:

1) Enabling the user to control the mouse on the screen using a smartphone. This includes controlling the mouse cursor as well as the left and right mouse buttons. For this purpose, we utilized the accelerometer data from the smartphone and the values of the four buttons (1 = clicked/pressed, 0 = not clicked/released) obtained through the DIPPID application.

2) Implementation of features that we deemed useful and could be realized through this interaction technique.

## Mouse Control

### Interaction Device
Can be used via Smartphone or M5Stack 

![geräte](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/62df0ea1-12a6-43a3-b5f2-ed0c27cd5c6b)

In theory, any device that can be lifted/rotated/moved, equipped with an accelerometer sensor and compatible with the DIPPID application can be used for interaction.

#### When using both devices for interaction, the following should be considered:
*The control of the mouse cursor, left and right mouse buttons, as well as the gesture feature (see "Features" section), is possible with both devices. However, some features that require a fourth button (see "Features" section) are not available with the M5Stack because it only has three physical buttons. In such cases, if you want to use all features, a smartphone with the DIPPID app, must be used instead.*

*It is also possible to experience disruptions when using the DIPPID app. We encountered two instances where, with the same code implementation, the control of the mouse cursor performed poorly on one occasion while working perfectly on the other. This disruption manifested as significant latency issues, resulting in outdated values being received. This problem occurred very rarely (2 times) and only when using the DIPPID app with a smartphone. Sometimes, restarting the smartphone helped resolve the issue. However, it always worked flawlessly with the M5Stack device (even when the disruption occurred simultaneously with the smartphone usage).*

### Mouse Movement

There are the following directions possible:

- standstill
- left, right
- up-left, up, up-right
- down-left, down, down-right
  
For the movement of the mouse cursor, the accelerometer data for the x-axis and y-axis are used. For the left and right directions, the x-value must exceed the threshold of 0.3 and -0.3, respectively. For the up and down directions, the y-value must exceed the threshold of 0.3 and -0.3, respectively. For the directions up-left, up-right, down-left, and down-right, both the x and y values must simultaneously exceed the threshold. 

If the threshold is not exceeded on both axes, the cursor remains in a standstill position.

When the respective threshold is exceeded, the movement occurs in the corresponding direction. The more the value is exceeded, the faster the cursor moves.

During the movement of the cursor, the speed is further increased gradually up to a maximum value, as even at maximum accelerometer x/y values, the speed would be too slow. When in standstill, the speed is reset. The origin scaling value depends on the size of the screen display. This ensures that the speed is consistent across different screen sizes. We have implemented this because we noticed that while the speed scaling worked for one of us, it was too fast for the other.

![dd](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/c5979707-fafb-4ac1-bd27-1f83187ca0d1)

## Method

For the implementation, we initially tried two approaches:

1. **Control based on raw accelerometer data**: In this approach, the cursor's direction and speed were determined based on the values obtained from the accelerometer.

2. **LSTM (Long Short-Term Memory) model**: In this approach, the trained model was fed with accelerometer data, and it made predictions about the direction of movement.

For this task, we initially divided ourselves and each experimented with a different approach. Surprisingly, the control based solely on accelerometer data worked remarkably well compared to the LSTM model variant. While the predictions in the LSTM variant were often incorrect initially, they improved as we increased the size of the training dataset. With a sufficiently large training dataset, we could expect the predictions to be very reliable. However, we decided against this approach because the control based solely on accelerometer data performed exceptionally well. A well-trained LSTM model would be expected to perform just as well as the control based solely on accelerometer data, but it would involve an additional processing step that would ultimately lead to the same result. There would still be a risk of misinterpreting certain values, which would not happen with the control based solely on accelerometer data.

## Mouse Buttons

The control of the left and right mouse buttons is done using Button 1 and Button 2 of the DIPPID application, respectively.

## Features

For the features, we use the accelerometer data (x and y) as well as the 4 DIPPID buttons and the one-dollar-recognizer for features with gesture recognition. 
Only the interaction device and the DIPPID application are used for all features. 

We have implemented the following features:

### 1.1 Gesture Feature: Screenshot
*Gesture-Feature: To draw a gesture, Button 3 is pressed and held in the DIPPID app while drawing with the mouse cursor. After releasing button 3, the drawn gesture is analyzed for recognition.*

The screenshot feature consists of two gestures. One gesture involves drawing a "v" shape, and the other involves drawing a checkmark.

![ddd](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/078b2b58-04c4-4d7f-a29b-b696f252d8d6)

For both gestures, a screenshot of the screen is taken. The difference lies in how the screenshot is handled afterward. When the "v" gesture is drawn, the screenshot is automatically saved in the "screenshots" folder. The storage location can be adjusted in the "Config.py" file under the "SCREENSHOT_FOLDER_PATH" section.

On the other hand, when a checkmark gesture is drawn, the screenshot is not automatically saved but instead copied to the clipboard. This allows the user to either paste the screenshot into an editor (e.g., Paint) for editing or paste it elsewhere without the need to save the screenshot permanently.

### 1.2 Gesture Feature: Application Launcer
*Gesture-Feature: To draw a gesture, Button 3 is pressed and held in the DIPPID app while drawing with the mouse cursor. After releasing button 3, the drawn gesture is analyzed for recognition.*

Similiar to a previous assignment, in a file called application.txt, paths to specific applications can be added. The name of the gesture in front of a path represent the corresponding gesture that launches the file. These gestures can also be changed if needed. It's important that the name of the gesture corresponds to a defined gesture in the file called gestures_enum.py.

### 1.3 Costum Gestures

### 2. Arrow-Key-Navigation 

This feature allows the arrow keys (up, down, left, and right) to be operated using the mouse cursor. When Button 4 is pressed and held, the movement direction of the cursor corresponds to the respective arrow key.

Here are two examples of its usage:

1. **Scrolling up or down**: The mouse cursor moves upwards (UP ARROW) or downwards (DOWN ARROW).

2. **Navigating presentation slides left or right**: The mouse cursor moves to the left (LEFT ARROW) or to the right (RIGHT ARROW) to jump between slides.

### 3. Copy-Paste 

This feature aims to accelerate the copy-paste process using the mouse by integrating "Ctrl + C" and "Ctrl + V" functionalities.

**COPY**: When text is selected by pressing and holding Button 1 (controls the left mouse button), it can be copied by continuing to hold Button 1 and simultaneously pressing Button 2.

**PASTE**: To paste the copied text somewhere else, press and hold Button 1 and simultaneously press Button 3.

While the copy-paste process can also be performed without this feature by using Button 2 (controls the right mouse button) and selecting "Copy" and later "Paste", this feature is designed to expedite the process and provide added convenience.

### 4. Virtuell Keyboard



## Start Application

mouse_app.py

## Quit Application

Key 'Q' on the keyboard

## Sensor Capabilities

Key 'Q' on the keyboard

Provides information about whether one or more capabilities (accelerometer, button 1, button 2, button 3, or button 4) are missing and which features would not function as a result.

## Code Structure

**mouse_app.py** -> starts the application

controller/**mouse_controller_class.py** -> logic

data/**gesture_template_dict.py** -> dict containing gesture templates

**enums** folder -> enums for the arrow keys and gestures

helper_classes -> different classes we created for our features

screenshots -> here the screenshoots taken are saved

Config.py -> for magic numbers and strings

DIPPID.py -> DIPPID functionalities

## Paper Source
[1] Ballagas, R., Rohs, M., & Sheridan, J. G. (2005, May). Mobile Phones as Pointing Devices. In PERMID (pp. 27-30). 
