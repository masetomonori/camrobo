#!/usr/bin/env python
#encoding: utf8
import unittest, rostest
import rosnode, rospy
import time
from camrobo.msg import MotorDirection

class MotorTest(unittest.TestCase):
    def setUp(self):
        pass

    def file_check(self, dev, value, message):
        with open("/dev/" + dev, "r") as f:
            self.assertEqual(f.readline(), str(value) + "\n", message)

    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/dc_motors', nodes, "node does not exist")

    def check_GPIO(self, left_dir, right_dir, a1, a2, b1, b2):
        pub = rospy.Publisher('/cmd_vel', MotorDirection)
        m = MotorDirection()
        m.left_dir  = left_dir
        m.right_dir = right_dir

        for i in range(10):
            pub.publish(m)
            time.sleep(0.1)

        self.file_check("dc_GPIO_06", a1, "wrong value from GPIO_06")
        self.file_check("dc_GPIO_13", a2, "wrong value from GPIO_13")
        self.file_check("dc_GPIO_20", b1, "wrong value from GPIO_20")
        self.file_check("dc_GPIO_21", b2, "wrong value from GPIO_21")


    def test_put_cmd_vel(self):
        self.check_GPIO( 1,  1, 1, 0, 1, 0) # forward
        self.check_GPIO( 1,  0, 1, 0, 0, 0) # right forward turn
        self.check_GPIO( 1, -1, 1, 0, 0, 1) # right spin turn
        self.check_GPIO( 0,  1, 0, 0, 1, 0) # left forward turn
        self.check_GPIO( 0,  0, 0, 0, 0, 0) # stop
        self.check_GPIO( 0, -1, 0, 0, 0, 1) # right backward turn
        self.check_GPIO(-1,  1, 0, 1, 1, 0) # left spin turn
        self.check_GPIO(-1,  0, 0, 1, 0, 0) # left backward turn
        self.check_GPIO(-1, -1, 0, 1, 0, 1) # backward

if __name__ == '__main__' :
    rospy.init_node('travis_test_dc_motors')
    rostest.rosrun('camrobo', 'travis_test_dc_motors', MotorTest)

