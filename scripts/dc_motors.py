#!/usr/bin/env python
#encoding: utf8
import sys, rospy
from camrobo.msg import MotorDirection 

#import RPi.GPIO as GPIO

class RRI_GPIO():
    def __init__(self):
        pass

    def setmode(self, bcm):
        pass

    def setwarnings(self, mode):
        pass

    def setup(self, pin, gin, pud_up = 0):
        pass
 
    def set_motor(A1,A2,B1,B2):
        rospy.loginfo(str(A1) + " " + str(A2) + str(B1) + " " + str(B2))
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

class DcMotors():
    def __init__(self):
        self.sub_cmd_vel1 = rospy.Subscriber('cmd_vel', MotorDirection, self.callback_cmd_vel)

        GPIO = RRI_GPIO()

        PIN = 18
        PWMA1 = 6
        PWMA2 = 13
        PWMB1 = 20
        PWMB2 = 21
        D1 = 12
        D2 = 26

        PWM = 50

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(PIN, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(PWMA1, GPIO.OUT)
        GPIO.setup(PWMA2, GPIO.OUT)
        GPIO.setup(PWMB1, GPIO.OUT)
        GPIO.setup(PWMB2, GPIO.OUT)
        GPIO.setup(D1, GPIO.OUT)
        GPIO.setup(D2, GPIO.OUT)
        p1 = GPIO.PWM(D1, 500)
        p2 = GPIO.PWM(D2,500)
        p1.start(50)
        p2.start(50)

    def callback_cmd_vel(self, message):
        l = message.left_dir
        r = message.right_dir

        a1 = 0
        a2 = 0
        b1 = 0
        b2 = 0

        if (l ==  1) : a1 = 1
        if (l == -1) : a2 = 1
        if (r ==  1) : b1 = 1
        if (r == -1) : b2 = 1
        
        set_motor(a1, a2, b1, b3)

if __name__ == '__main__':
    rospy.init_node('dc_motors')
    m = DcMotors()

    rospy.loginfo("waiting for dc_motors input")

    rospy.spin()
