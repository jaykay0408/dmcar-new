'''
**********************************************************************
* Filename    : test-control.py
* Description : test control for servo
* Update      : Lee    2021-09-01    New release
**********************************************************************
'''
# Import New Picar Libraries
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)

from picarmini import dir_servo_angle_calibration
from picarmini import forward
from ezblock import delay
from picarmini import backward
from picarmini import set_dir_servo_angle
from picarmini import stop

SPEED = 0
forward(0)

while True:
    key = input("> ")
    SPEED = 30

    if key == 'q':
        break
    elif key == 'w':
        forward(SPEED)
    elif key == 'x':
        backward(SPEED)
    elif key == 'a':
        set_dir_servo_angle(-25)
    elif key == 'd':
        set_dir_servo_angle(25)
    elif key == 's':
        set_dir_servo_angle(0)
    elif key == 'z':
        set_dir_servo_angle(0)
        forward(0)
        stop()


