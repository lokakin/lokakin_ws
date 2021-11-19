#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
import random

def talker():
	rospy.init_node("talker_node", anonymous=True)
	pub = rospy.Publisher("talker_topic", Int32, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		msg = (random.randrange (0,1000))
		rospy.loginfo("Data sent")
		pub.publish(msg)
		rate.sleep()

if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass