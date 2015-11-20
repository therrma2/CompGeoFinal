#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
import tf
from geometry_msgs.msg import Point

def main():
    rospy.init_node('markers')
    m1 = Marker()
    m1.lifetime.secs = 0
    pub = rospy.Publisher('markers', Marker, queue_size = 10)
    rospy.sleep(3)
    m1.header.stamp = rospy.Time.now()
    m1.header.frame_id = "/base_link"
    m1.ns = "m1"
    m1.type = 3
    m1.action = 0
   
    m1.pose.position.x = 1
    m1.pose.position.y = .5
    m1.pose.position.z = .15

    m1.color.r = 1
    m1.color.g = 0
    m1.color.b = 0
    m1.color.a = 1
    print m1.pose
    m1.scale.x = .1
    m1.scale.y = .1
    m1.scale.z = .3
    print m1

    pub.publish(m1)
    while not rospy.is_shutdown():
        rospy.spin()



if __name__ == '__main__':

    main()
