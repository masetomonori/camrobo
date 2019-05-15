#!/usr/bin/env python
#encoding: utf8
import sys, rospy
import time
from camrobo.msg import MotorDirection 

from PCA9685 import PCA9685

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)
speed = 100

class DcMotors():
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0

    def __init__(self):
        self.sub_cmd_vel1 = rospy.Subscriber('cmd_vel', MotorDirection, self.callback_cmd_vel)

        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def move_motor(self):
        pwm.setDutycycle(self.PWMA, speed)
        pwm.setDutycycle(self.PWMA, speed)

        pwm.setLevel(self.AIN1, self.a1)
        pwm.setLevel(self.AIN2, self.a2)
        pwm.setLevel(self.BIN1, self.b1)
        pwm.setLevel(self.BIN2, self.b2)

        #rospy.loginfo(str(self.a1) + " " + str(self.a2) + " " + str(self.b1) + " " + str(self.b2))

    def callback_cmd_vel(self, message):
        l = message.left_dir
        r = message.right_dir

        if (l == 0) :
            self.a1 = 0
            self.a2 = 0
        if (r == 0) :
            self.b1 = 0
            self.b2 = 0

        if (l ==  1) :
            self.a1 = 1
            self.a2 = 0
        if (l == -1) :
            self.a1 = 0
            self.a2 = 1
        if (r ==  1) :
            self.b1 = 1
            self.b2 = 0
        if (r == -1) :
            self.b1 = 0
            self.b2 = 1
        
if __name__ == '__main__':
    rospy.init_node('dc_motors')
    m = DcMotors()

    rospy.loginfo("waiting for dc_motors input")

    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        m.move_motor()
        rate.sleep()


