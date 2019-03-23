#!/usr/bin/env python
#encoding: utf8
import sys, rospy
import time
from camrobo.msg import MotorDirection 

import RPi.GPIO as GPIO

class DcMotors():
    #GPIO = RRI_GPIO()  # temp

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

        #GPIO = RRI_GPIO()  # temp

        #PIN = 18
        #PWMA1 = 6
        #PWMA2 = 13
        #PWMB1 = 20
        #PWMB2 = 21
        #D1 = 12
        #D2 = 26

        #PWM = 50

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.PIN, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.PWMA1, GPIO.OUT)
        GPIO.setup(self.PWMA2, GPIO.OUT)
        GPIO.setup(self.PWMB1, GPIO.OUT)
        GPIO.setup(self.PWMB2, GPIO.OUT)
        GPIO.setup(self.D1, GPIO.OUT)
        GPIO.setup(self.D2, GPIO.OUT)
        p1 = GPIO.PWM(self.D1, 500)
        p2 = GPIO.PWM(self.D2,500)
        p1.start(50)
        p2.start(50)

        #while True:
            #GPIO.output(self.PWMA1,1)
            #GPIO.output(self.PWMA2,0)
            #GPIO.output(self.PWMB1,1)
            #GPIO.output(self.PWMB2,0)


    def set_motor(self, A1,A2,B1,B2):
        #GPIO = RRI_GPIO()  # temp
        rospy.loginfo(str(A1) + " " + str(A2) + " " + str(B1) + " " + str(B2))

        p1 = GPIO.PWM(self.D1, 500)
        p2 = GPIO.PWM(self.D2, 500)

        p1.start(50)
        p2.start(50)

        for i in range(10000):#while True:
            GPIO.output(self.PWMA1,A1)
            GPIO.output(self.PWMA2,A2)
            GPIO.output(self.PWMB1,B1)
            GPIO.output(self.PWMB2,B2)

        pass

    def move_motor(self):
        GPIO.output(self.PWMA1,self.a1)
        GPIO.output(self.PWMA2,self.a2)
        GPIO.output(self.PWMB1,self.b1)
        GPIO.output(self.PWMB2,self.b2)

        rospy.loginfo(str(self.a1) + " " + str(self.a2) + " " + str(self.b1) + " " + str(self.b2))

    def callback_cmd_vel(self, message):
        l = message.left_dir
        r = message.right_dir

        #a1 = 0
        #a2 = 0
        #b1 = 0
        #b2 = 0

        if (l == 0) :
            self.a1 = 0
            self.a2 = 0
        if (r == 0) :
            self.b1 = 0
            self.b2 = 0

        if (l ==  1) : self.a1 = 1
        if (l == -1) : self.a2 = 1
        if (r ==  1) : self.b1 = 1
        if (r == -1) : self.b2 = 1
        
        #while True:  
        #self.set_motor(a1, a2, b1, b2)
            #time.sleep(1)

if __name__ == '__main__':
    rospy.init_node('dc_motors')
    m = DcMotors()

    rospy.loginfo("waiting for dc_motors input")

    #while True :

    #    time.sleep(0.00006)    

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        m.move_motor()
        rate.sleep()
