import serial
import os
import numpy as np
import matplotlib.pyplot as plt

script_path =  os.path.dirname(os.path.realpath(__file__))


with open(script_path + "/data.py", "w+") as data_file:
    pass # create empty file

ser = serial.Serial('/dev/ttyUSB0', 921600)

while ser.read() != b'\n':
    pass
while True:
    try:
        reading = ser.readline().decode('utf-8')

        values = reading.strip().split(" ")

        values = [value + "\n" for value in values]

        with open(script_path + "/data.py", "w+") as data_file:
            data_file.writelines(values)

    except KeyboardInterrupt:
        ser.close()