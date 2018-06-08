#!/usr/bin/env python
import rospy
from my_awesone_code.msg import Complex

def callback(msg):
    print('Real: {}'.format(msg.real))
    print('Imaginary: {}'.format(msg.imaginary))
    print()

rospy.init_node('message_subscriber')

sub = rospy.Subscriber('complex', Complex, callback)

rospy.spin()
