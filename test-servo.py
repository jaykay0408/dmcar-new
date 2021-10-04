'''
**********************************************************************
* Filename    : test-servo.py
* Description : test for server
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

SPEED = 30

# ============== Back wheels =============
# 'bwready':
#forward(SPEED)

for i in range(10, 101,10):
    forward(i)
    time.sleep(2)

# 'forward':
forward(SPEED)
time.sleep(1)

# 'backward':
backward(SPEED)
time.sleep(1)

# 'stop':
stop()

# ============== Front wheels =============
# Turn Left
set_dir_servo_angle(-30)
time.sleep(1)

# Straight
set_dir_servo_angle(0)
time.sleep(1)

# Turn Right
set_dir_servo_angle(30)
time.sleep(1)

# Straight
set_dir_servo_angle(0)
time.sleep(1)

# Angle 45 degree to 135 degree
for i in range(45, 135, 5):
    print(i)
    set_dir_servo_angle(i-90)
    time.sleep(1)

set_dir_servo_angle(0)
stop()
