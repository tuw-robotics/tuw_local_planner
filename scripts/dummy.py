#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from tf.transformations import euler_from_quaternion, quaternion_from_euler

class Dummy:

    def __init__(self):
        self.pub_cmd = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.pub_laser = rospy.Publisher('debug_scan', LaserScan, queue_size=10)
        self.sub_laser = rospy.Subscriber( 'base_scan', LaserScan, self.callback_laser)
        self.sub_odom = rospy.Subscriber( 'odom', Odometry, self.callback_odom)
        self.timer = rospy.Timer(rospy.Duration(0.1), self.callback_timer)

        self.laser = LaserScan()
        self.odom =  Odometry()

    def callback_laser(self, laser):
        rospy.loginfo("laser")
        cmd = Twist()
        cmd.linear.x = 0.1
        self.pub_cmd.publish(cmd)

    def callback_odom(self, odom):
        rospy.loginfo("odom")
        self.odom = odom
        q = self.odom.pose.pose.orientation
        (roll, pitch, yaw) = euler_from_quaternion ([q.x, q.y, q.z, q.w])
        print (yaw)

    def callback_timer(self, timer):
        rospy.loginfo("callback_timer")

if __name__ == '__main__':
    rospy.init_node('dummy', anonymous=True)
    try:
        dummy = Dummy()
        rospy.spin()
    except rospy.ROSInterruptException:
        print("exception thrown")
        pass
