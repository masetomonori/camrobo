#!/usr/bin/env python
#encoding: utf8
import unittest, rostest
import rosnode, rospy
import time
from sensor_msgs.msg import Joy

class ControllerTest(unittest.TestCase):
    def setUp(self):
        pass

    def file_check(self, dev, value, message):
        with open("/dev/" + dev, "r") as f:
            self.assertEqual(f.readline(), str(value) + "\n", message)

    def test_node_exist(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/camrobo_cmd_vel', nodes, "node does not exist")

    def test_put_motor_direction(self):
        #pub = rospy.Publisher('/motor_raw', MotorFreqs)
        #m = MotorFreqs()
        #m.left_hz = 123
        #m.right_hz = 456
        #for i in range(10):
        #    pub.publish(m)
        #    time.sleep(0.1)

        #self.file_check("rtmotor_raw_l0", m.left_hz,  "wrong left value from motor_raw")
        #self.file_check("rtmotor_raw_r0", m.right_hz, "wrong right value from motor_raw")
        pass

    def test_put_joy(self):
        pub = rospy.Publisher('/joy', Joy)
        j = Joy()
        j.axes = [0.0, 0.0, 0.0, 0.95, 0.0, 0.9]
        
        for i in range(10):
            pub.publish(j)
            time.sleep(0.1)
  
        self.file_check("dc_GPIO_06", 1, "wrong value from GPIO_06")
        self.file_check("dc_GPIO_13", 0, "wrong value from GPIO_13")
        self.file_check("dc_GPIO_20", 1, "wrong value from GPIO_20")
        self.file_check("dc_GPIO_21", 0, "wrong value from GPIO_21")


        #self.file_check("rtmotor_raw_l0", 200, "wrong left value from cmd_vel")
        #self.file_check("rtmotor_raw_r0", 600, "wrong right value from cmd_vel")

        #time.sleep(1.1)
        #self.file_check("rtmotor_raw_r0", 0, "don't stop after 1[s]")
        #self.file_check("rtmotor_raw_l0", 0, "don't stop after 1[s]")
        pass

if __name__ == '__main__' :
    rospy.init_node('travis_test_camrobo_controller')
    rostest.rosrun('camrobo', 'travis_test_camrobo_controller', ControllerTest)

