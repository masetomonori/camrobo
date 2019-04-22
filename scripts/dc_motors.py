#!/usr/bin/env python
#encoding: utf8
import sys, rospy
import time
from camrobo.msg import MotorDirection 

try:
    import RPi.GPIO as GPIO            # for raspberry pi
except:
    from pseudo_rpi_gpio import GPIO   # for PC debug

class DcMotors():
    PIN = 18
    PWMA1 = 6
    PWMA2 = 13
    PWMB1 = 20
    PWMB2 = 21
    D1 = 12
    D2 = 26

    PWM = 50

    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0

    def __init__(self):
        self.sub_cmd_vel1 = rospy.Subscriber('cmd_vel', MotorDirection, self.callback_cmd_vel)

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.PIN, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.PWMA1, GPIO.OUT)
        GPIO.setup(self.PWMA2, GPIO.OUT)
        GPIO.setup(self.PWMB1, GPIO.OUT)
        GPIO.setup(self.PWMB2, GPIO.OUT)
        GPIO.setup(self.D1, GPIO.OUT)
        GPIO.setup(self.D2, GPIO.OUT)

    def move_motor(self):
        p1 = GPIO.PWM(self.D1, 500)
        p2 = GPIO.PWM(self.D2, 500)
        #p1 = GPIO.PWM(self.D1, 600)
        #p2 = GPIO.PWM(self.D2, 600)
        #p1.start(50)
        #p2.start(50)
        p1.start(75)
        p2.start(75)

        GPIO.output(self.PWMA1,self.a1)
        GPIO.output(self.PWMA2,self.a2)
        GPIO.output(self.PWMB1,self.b1)
        GPIO.output(self.PWMB2,self.b2)

        #rospy.loginfo(str(self.a1) + " " + str(self.a2) + " " + str(self.b1) + " " + str(self.b2))

    def callback_cmd_vel(self, message):
        l = message.left_dir
        r = message.right_dir

        if (l == 0) :
            self.a1 = 0
            self.a2 = 0
        if (r == 0) :
            self.b1 = 0
            self.b2 = 0

        if (l ==  1) :
            self.a1 = 1
            self.a2 = 0
        if (l == -1) :
            self.a1 = 0
            self.a2 = 1
        if (r ==  1) :
            self.b1 = 1
            self.b2 = 0
        if (r == -1) :
            self.b1 = 0
            self.b2 = 1
        
if __name__ == '__main__':
    rospy.init_node('dc_motors')
    m = DcMotors()

    rospy.loginfo("waiting for dc_motors input")

    #rate = rospy.Rate(100)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        m.move_motor()
        rate.sleep()


