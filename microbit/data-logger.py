from microbit import *
import time

start_time = running_time()
duration = 20000  # milliseconds = 20 seconds

while running_time() - start_time < duration:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    t = running_time() - start_time  # time since recording started
    print("{},{},{},{}".format(t, x, y, z))
    sleep(100)  # sample every 100ms
