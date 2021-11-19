#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def myCallBack(data):
    rospy.loginfo(rospy.get_caller_id()+" receiving... . %s ",data.data)



def listener():
	rospy.init_node("listener_node", anonymous=True)
	rospy.Subscriber("talker_topic", Int32, myCallBack)
	rospy.spin()

if __name__ == "__main__":
	listener()