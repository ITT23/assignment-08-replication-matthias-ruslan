# Extending/Implementing the interaction technique described in the paper "Mobile Phones as Pointing Devices" with DIPPID
Paper by Ballagas et al. [1]

## Team 

### Matthias Dobiosz

![Matthias](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/5e58eed8-648c-4788-be6a-c25620acc1c5)

### Ruslan Asabidi 

![me](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/cc4b40f7-e27e-487a-8f29-2e624d3f414b)



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
The control of the mouse cursor, left and right mouse buttons, as well as the gesture feature (see "Features" section), is possible with both devices. However, some features that require a fourth DIPPID button (see "Features" section) are not available with the M5Stack because it only has three physical buttons. In such cases, a smartphone with the DIPPID app, which has four buttons, must be used instead.

### Mouse Movement

There are the following directions possible:

- Standstill
- Up-left, up, up-right
- Down-left, down, down-right
  
For the movement of the mouse cursor, the accelerometer data for the x-axis and y-axis are used. For the left and right directions, the x-value must exceed the threshold of 0.3 and -0.3, respectively. For the up and down directions, the y-value must exceed the threshold of 0.3 and -0.3, respectively. For the directions up-left, up-right, down-left, and down-right, both the x and y values must simultaneously exceed the threshold. 

If the threshold is not exceeded on both axes, the cursor remains in a standstill position.

When the respective threshold is exceeded, the movement occurs in the corresponding direction. The more the value is exceeded, the faster the cursor moves.

During the movement of the cursor, the speed is further increased gradually up to a maximum value, as even at maximum accelerometer x/y values, the speed would be too slow. When in standstill, the speed is reset. The origin scaling value depends on the size of the screen display. This ensures that the speed is consistent across different screen sizes. We have implemented this because we noticed that while the speed scaling worked for one of us, it was too fast for the other.

![dd](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/c5979707-fafb-4ac1-bd27-1f83187ca0d1)

### Mouse Buttons

The control of the left and right mouse buttons is done using Button 1 and Button 2 of the DIPPID application, respectively.







## Gestures

To start recording a gesture hold button_3. The gestures are performed by "drawing" one of the predefined symbols with the mouse anywhere on the screen.

## Paper Source
[1] Ballagas, R., Rohs, M., & Sheridan, J. G. (2005, May). Mobile Phones as Pointing Devices. In PERMID (pp. 27-30).

### Application Launcher

Similiar to a previous assignment, in a file called application.txt, paths to specific applications can be added. The name of the gesture in front of a path represent the corresponding gesture that launches the file. These gestures can also be changed if needed. It's important that the name of the gesture corresponds to a defined gesture in the file called gestures_enum.py. 
