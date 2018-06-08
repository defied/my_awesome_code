#!/usr/bin/env python
import rospy
# Here is where we import the new message we made in /msg
from my_awesone_code.msg import Complex
from random import random


rospy.init_node('message_publisher')

pub = rospy.Publisher('complex', Complex)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
    msg = Complex()
    random_data = random()
    msg.real = random()
    msg.imaginary = random()
    pub.publish(msg)
    rate.sleep()
