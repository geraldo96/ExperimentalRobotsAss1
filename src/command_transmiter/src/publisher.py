#!/usr/bin/env python
import rospy
from fsm_receiver.msg import Command

def talker():
    pub = rospy.Publisher('chatter_command', Command, queue_size=10)
    rospy.init_node('custom_talker', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = Command()
    msg.state = 1
    msg.x = 4
    msg.y = 4
    

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
