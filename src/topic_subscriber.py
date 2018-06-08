#!/usr/bin/env python

#required import
import rospy
# As this is another dependancy, we have to add <depend>std_msgs"</depend> to the package.xml file.
from std_msgs.msg import Int32

# Any functions
def callback(msg):
    ''' A simple method to print published  information from subscribed topic'''
    print(msg.data)

# Initialize the node
rospy.init_node('topic_subscriber')

# Subscribe the node to a topic including the callback function
pub = rospy.Subscriber('counter', Int32, callback)

# Give control to ROS. This function will only return when the node is ready to shutdown
# Avoids having to create a while loop in this script
rospy.spin()
