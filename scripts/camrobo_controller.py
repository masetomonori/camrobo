#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import time
from sensor_msgs.msg import Joy
from camrobo.msg import MotorDirection

class CamroboController(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self._md_pub = rospy.Publisher('/cmd_vel', MotorDirection, queue_size=1)

    def joy_callback(self, joy_msg):
        motor_dir = MotorDirection()
        motor_dir.right_dir = 0
        motor_dir.left_dir = 0        
        
        #rospy.loginfo(str(joy_msg.axes[3]) + " " + str(joy_msg.axes[5]))

        if joy_msg.axes[3] >  0.9 :    # right axes up
           motor_dir.right_dir =  1
        if joy_msg.axes[3] < -0.9 :    # right axes down
           motor_dir.right_dir = -1
       
        if joy_msg.axes[5] >  0.9 :    # left axes up
           motor_dir.left_dir =  1
        if joy_msg.axes[5] < -0.9 :    # left axes down
           motor_dir.left_dir = -1

        self._md_pub.publish(motor_dir)

if __name__ == '__main__':
    rospy.init_node('camrobo_cmd_vel')
    camrobo_cmd_vel = CamroboController()

    rospy.loginfo("waiting for controller input")

    rospy.spin()

