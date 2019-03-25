#!/usr/bin/env python
#encoding: utf8
import sys, rospy

class pseudo_rpi_gpio():
    def __init__(self):
        pass

    def setmode(self, bcm):
        pass

    def setwarnings(self, mode):
        pass

    def setup(self, pin, gin, pud_up = 0):
        pass

    def output(self, pwm, n):
        #rospy.loginfo(str(pwm) + " " + str(n))
        pass
 
    class PWM():
        def __init__(self, d, n):
            pass

        def start(self, n):
            pass

    class BCM():
        pass

    class IN():
        pass

    class PUD_UP():
        pass

    class OUT():
        pass

GPIO = pseudo_rpi_gpio()
