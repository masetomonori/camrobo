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
        dev_file_name = "/dev/dc_GPIO_" + str(pwm).zfill(2)
        try:
            with open(dev_file_name, 'w') as dev:
                dev.write(str(n) + "\n")
        except:
            #rospy.logerr("cannot write to " + dev_file_name)
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
