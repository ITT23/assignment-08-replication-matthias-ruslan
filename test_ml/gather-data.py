# this program gathers sensor data
import time
from DIPPID import SensorUDP
import csv

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

capture_data = False
start_time = 0
label = "bottom_right"
number = 3

headers = ['timestamp', 'accelerometer_x', 'accelerometer_y',
           'accelerometer_z', 'gyroscope_x', 'gyroscope_y', 'gyroscope_z',
           'activity']
data = []


def save_data():
    with open('./data/data_' + label + '_' + str(number) + '.csv', 'w',
              encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(headers)
        writer.writerows(data)


while (True):
    if sensor.has_capability('button_1'):
        button_1 = sensor.get_value('button_1')
        if int(button_1) == 1 and not capture_data:
            print("data collection started")
            capture_data = True
            start_time = time.time()

        if capture_data:
            duration = round(time.time() - start_time, 2)

            if sensor.has_capability('accelerometer'):
                acc_x = float(sensor.get_value('accelerometer')['x'])
                acc_y = float(sensor.get_value('accelerometer')['y'])
                acc_z = float(sensor.get_value('accelerometer')['z'])

            if sensor.has_capability('gyroscope'):
                gyr_x = float(sensor.get_value('gyroscope')['x'])
                gyr_y = float(sensor.get_value('gyroscope')['y'])
                gyr_z = float(sensor.get_value('gyroscope')['z'])

            data.append(
                [duration, acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z, label])

            if duration > 5:
                save_data()
                print("end of data collection")
                break

    time.sleep(0.01)
