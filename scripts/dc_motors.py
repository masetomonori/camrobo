#!/usr/bin/env python
#encoding: utf8
import sys, rospy
from camrobo.msg import MotorDirection 

class DcMotors():
    def __init__(self):
        self.sub_cmd_vel1 = rospy.Subscriber('cmd_vel', MotorDirection, self.callback_cmd_vel)

    def callback_cmd_vel(self, message):
        a = message.left_dir
        b = message.right_dir

        rospy.loginfo(str(a) + " " + str(b))        

if __name__ == '__main__':
    rospy.init_node('dc_motors')
    m = DcMotors()

    rospy.loginfo("waiting for dc_motors input")

    rospy.spin()
