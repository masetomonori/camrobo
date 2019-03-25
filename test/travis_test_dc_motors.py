#!/usr/bin/env python
#encoding: utf8
import unittest, rostest
import rosnode, rospy
import time

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

    def test_put_cmd_vel(self):
        #pub = rospy.Publisher('/cmd_vel', Twist)
        #m = Twist()
        #m.linear.x = 0.1414
        #m.angular.z = 1.57
        #for i in range(10):
        #    pub.publish(m)
        #    time.sleep(0.1)

        #self.file_check("rtmotor_raw_l0", 200, "wrong left value from cmd_vel")
        #self.file_check("rtmotor_raw_r0", 600, "wrong right value from cmd_vel")

        #time.sleep(1.1)
        #self.file_check("rtmotor_raw_r0", 0, "don't stop after 1[s]")
        #self.file_check("rtmotor_raw_l0", 0, "don't stop after 1[s]")
        pass

if __name__ == '__main__' :
    rospy.init_node('travis_test_dc_motors')
    rostest.rosrun('camrobo', 'travis_test_dc_motors', MotorTest)

