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

## Paper Source
[1] Ballagas, R., Rohs, M., & Sheridan, J. G. (2005, May). Mobile Phones as Pointing Devices. In PERMID (pp. 27-30).

## Our Motivation

We found the idea of ​​using a smartphone to control the mouse very interesting. Especially with regard to the fact that we can implement the control using DIPPID. The study by Alex et al. is from 2005 and accordingly the options were limited. An external bulky accelerometer had to be attached for the study. 

![handy](https://github.com/ITT23/assignment-08-replication-matthias-ruslan/assets/41992838/5aa2de5c-2158-4406-9f91-f85e31bb9d62)

Most smartphones in the lower price segment now have at least one integrated accelerometer. In addition, there are also sensors that provide gyroscope and angle data, among other things. The DIPPID functionality used in the course lends itself very well to expanding and implementing the approach presented in the paper. On the one hand, the data from the various sensors can be obtained and processed very easily using the DIPPID app, and on the other hand, the 3 buttons allow you to control the mouse buttons.

## Our Goal

We would like to implement the mouse control using variants and compare them with each other.

1.) Control only via DIPED sensor data.
2.) LSTM

We would also like to add other features such as latency options and other functions.

## Mouse Control

Can be used via Smartphone or M5Stack 

1) You can tilt the device in both axes to move the mouse correspondingly
2) Use button_1 to simulate a left mouse click
3) Use button_2 to simulate a right mouse click

## Gestures

To start recording a gesture hold button_3. The gestures are performed by "drawing" one of the predefined symbols with the mouse anywhere on the screen.

### Application Launcher

Similiar to a previous assignment, in a file called application.txt, paths to specific applications can be added. The name of the gesture in front of a path represent the corresponding gesture that launches the file. These gestures can also be changed if needed. It's important that the name of the gesture corresponds to a defined gesture in the file called gestures_enum.py. 
