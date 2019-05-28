#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import time
from sensor_msgs.msg import Joy
from camrobo.msg import MotorDirection
from joy_map import JoyMap
import os 

class CamroboController(object):

    jm = JoyMap()
    shutdown_count = 0

    def __init__(self):
        self._joy_sub = rospy.Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self._md_pub = rospy.Publisher('/cmd_vel', MotorDirection, queue_size=1)

    def joy_callback(self, joy_msg):
        #print(joy_msg)
        if joy_msg.buttons[self.jm.button_A] == 1:
            self.shutdown_count +=1
            if self.shutdown_count >= 100:
                sudoPassword = 'raspberry'
                command = 'shutdown -h now'
                p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
            return
        
        motor_dir = MotorDirection()
        motor_dir.right_dir = 0
        motor_dir.left_dir = 0        
 
        rospy.loginfo("l:" + str(joy_msg.axes[self.jm.axis_stick_v_l]) + ", r:" + str(joy_msg.axes[self.jm.axis_stick_v_r]))

        #print(self.jm.axis_stick_v_r, self.jm.axis_stick_v_l)

        if joy_msg.axes[self.jm.axis_stick_v_r] >  0.9 :    # right axes up
           motor_dir.right_dir =  1
        if joy_msg.axes[self.jm.axis_stick_v_r] < -0.9 :    # right axes down
           motor_dir.right_dir = -1

        if joy_msg.axes[self.jm.axis_stick_v_l] >  0.9 :    # left axes up
           motor_dir.left_dir =  1
        if joy_msg.axes[self.jm.axis_stick_v_l] < -0.9 :    # left axes down
           motor_dir.left_dir = -1

        self.shutdown_count = 0

        self._md_pub.publish(motor_dir)

if __name__ == '__main__':
    rospy.init_node('camrobo_cmd_vel')
    camrobo_cmd_vel = CamroboController()

    rospy.loginfo("waiting for controller input")

    rospy.spin()

