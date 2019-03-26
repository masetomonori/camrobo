#!/usr/bin/env python
#encoding: utf8
import unittest, rostest
import rosnode, rospy
import time
from camrobo.msg import MotorDirection

class MotorTest(unittest.TestCase):
    def setUp(self):
        #rospy.wait_for_service('/motor_on')
        #rospy.wait_for_service('/motor_off')
        #rospy.wait_for_service('/timed_motion')
        #on = rospy.ServiceProxy('motor_on', Trigger)
        #ret = on()
        pass

    def file_check(self, dev, value, message):
        with open("/dev/" + dev, "r") as f:
            self.assertEqual(f.readline(), str(value) + "\n", message)

    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/dc_motors', nodes, "node does not exist")

    def test_put_cmd_vel(self):
        pub = rospy.Publisher('/cmd_vel', MotorDirection)
        m = MotorDirection()
        m.left_dir  = -1
        m.right_dir = -1
        for i in range(10):
            pub.publish(m)
            time.sleep(0.1)

        self.file_check("dc_GPIO_06", 0, "wrong value from GPIO_06")
        self.file_check("dc_GPIO_13", 1, "wrong value from GPIO_13")
        self.file_check("dc_GPIO_20", 0, "wrong value from GPIO_20")
        self.file_check("dc_GPIO_21", 1, "wrong value from GPIO_21")
      
        pass

if __name__ == '__main__' :
    rospy.init_node('travis_test_dc_motors')
    rostest.rosrun('camrobo', 'travis_test_dc_motors', MotorTest)

