#!/usr/bin/env python
import rospy
from position_receiver.msg import Position

def callback(data):
    rospy.loginfo("The position to reach is : %d , %d" % (data.x,data.y))
    
def listener():


    rospy.init_node('listener_position', anonymous=True)

    rospy.Subscriber("chatter_position", Position, callback)

    
    rospy.spin()

if __name__ == '__main__':
    listener()
