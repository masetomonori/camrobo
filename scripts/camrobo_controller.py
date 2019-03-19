#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from sensor_msgs.msg import Joy
from camrobo.msg import MotorDirection

class CamroboController(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self._md_pub = rospy.Publisher('/cmd_vel', MotorDirection, queue_size=1)

        self.level = 1

    def limitter(self, lvl):
        if lvl <= 0:    return 1
        if lvl >= 6:    return 5
        return lvl

    def joy_callback(self, joy_msg):
        if joy_msg.buttons[7] == 1: self.level += 1
        if joy_msg.buttons[6] == 1: self.level -= 1
        self.level = self.limitter(self.level)

        twist = Twist()
        if joy_msg.buttons[0] == 1:
            twist.linear.x = joy_msg.axes[1] * 0.2 * self.level
            twist.angular.z = joy_msg.axes[0] * 3.14 / 32 * (self.level + 15)
        else:
            twist.linear.x = 0
            twist.angular.z = 0
        self._twist_pub.publish(twist)

        if joy_msg.axes[1] == joy_msg.axes[0] == 0:
            self.level -= 1


if __name__ == '__main__':
    rospy.init_node('camrobo_cmd_vel')
    camrobo_cmd_vel = CamroboController()

    rospy.loginfo("waiting for controller input")

    rospy.spin()

