#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
  
def publish_message():

  pub = rospy.Publisher('video_frames', Image, queue_size=10)
  rospy.init_node('webcam_pub', anonymous=True)
  rate = rospy.Rate(10) # 10hz

  faceCascade = cv2.CascadeClassifier('/home/lokakin/lokakin_ws/src/lokakin/scripts/question3/haarcascade_frontalface_default.xml')

  cap = cv2.VideoCapture(0)
     
  # Used to convert between ROS and OpenCV images
  br = CvBridge()
 
  while not rospy.is_shutdown():
      ret, frame = cap.read()
         
      if ret == True:
        imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray, 1.1, 3)
        for (x,y,w,h) in faces:
          cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
        rospy.loginfo('publishing video frame')
        pub.publish(br.cv2_to_imgmsg(frame))
      rate.sleep()
         
if __name__ == '__main__':
  try:
    publish_message()
  except rospy.ROSInterruptException:
    pass