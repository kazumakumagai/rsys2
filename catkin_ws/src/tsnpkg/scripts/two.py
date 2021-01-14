#!/usr/bin/env python3
## coding: UTF-8

import rospy
import time
from std_msgs.msg import String

def callback(message):
        rospy.loginfo("robosys! [%s]", message.data) # ターミナルへの表示
        print(time.gmtime())
rospy.init_node('listener')
sub = rospy.Subscriber('chatter', String, callback) # chatterというTopicを受信！受信したら上で定義したcallback関数を呼ぶ
rospy.spin()
