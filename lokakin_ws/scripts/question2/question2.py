#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

def talker():
	a=10
	rospy.init_node("publisher_node", anonymous=True)
	pub = rospy.Publisher("talker_topic", Int16, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		for a in range(10,171,20):
			pub.publish(a)
			rate.sleep()
			print(a)
			if a==170: 
				for a in range(170,10,-20):
					pub.publish(a)
					rate.sleep()
					print(a)


if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


  

