#!/usr/bin/env python

#required import
import rospy
# As this is another dependancy, we have to add <depend>std_msgs"</depend> to the package.xml file.
from std_msgs.msg import Int32

# Initialize the node
rospy.init_node('topic_publisher')

# Advertise the node with a Publisher ('topic')
pub = rospy.Publisher('counter', Int32)

# How often do we publish (in hz)
rate = rospy.Rate(2)

# Main
count = 0

# Ensure this only runs while rospy is active.
while not rospy.is_shutdown():
    # Publish (content)
    pub.publish(count)
    count += 1
    # Sleep for (hz)
    rate.sleep()

