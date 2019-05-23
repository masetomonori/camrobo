#!/usr/bin/env python
#encoding: utf8
import unittest, rostest
import rosnode, rospy
import time
from sensor_msgs.msg import Joy
from joy_map import JoyMap

class ControllerTest(unittest.TestCase):

    jm = JoyMap()

    def setUp(self):
        pass

    def file_check(self, dev, value, message):
        with open("/dev/" + dev, "r") as f:
            self.assertEqual(f.readline(), str(value) + "\n", message)

    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/camrobo_cmd_vel', nodes, "node does not exist")

    def check_GPIO(self, left_axes, right_axes, a1, a2, b1, b2):
	pub = rospy.Publisher('/joy', Joy)
        j = Joy()
        j.axes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        j.axes[self.jm.axis_stick_v_r] = right_axes
        j.axes[self.jm.axis_stick_v_l] = left_axes

        for i in range(10):
            pub.publish(j)
            time.sleep(0.1)

        self.file_check("dc_GPIO_06", a1, "wrong value from GPIO_06")
        self.file_check("dc_GPIO_13", a2, "wrong value from GPIO_13")
        self.file_check("dc_GPIO_20", b1, "wrong value from GPIO_20")
        self.file_check("dc_GPIO_21", b2, "wrong value from GPIO_21")

    def test_put_joy(self):
        self.check_GPIO( 0.95,  0.95, 1, 0, 1, 0) # forward
        self.check_GPIO( 0.95,  0.0 , 1, 0, 0, 0) # right forward turn
        self.check_GPIO( 0.95, -0.95, 1, 0, 0, 1) # right spin turn
        self.check_GPIO( 0.0 ,  0.95, 0, 0, 1, 0) # left forward turn
        self.check_GPIO( 0.0 ,  0.0 , 0, 0, 0, 0) # stop
        self.check_GPIO( 0.0 , -0.95, 0, 0, 0, 1) # right backward turn
        self.check_GPIO(-0.95,  0.95, 0, 1, 1, 0) # left spin turn
        self.check_GPIO(-0.95,  0.0 , 0, 1, 0, 0) # left backward turn
        self.check_GPIO(-0.95, -0.95, 0, 1, 0, 1) # backward

if __name__ == '__main__' :
    rospy.init_node('travis_test_camrobo_controller')
    rostest.rosrun('camrobo', 'travis_test_camrobo_controller', ControllerTest)

