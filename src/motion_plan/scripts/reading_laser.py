#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan


def clbk_laser(msg):
    # 720 samles into 5 regions
    max_distance = 10
    regions = [
            min(max_distance, min(msg.ranges[0:144])),
            min(max_distance, min(msg.ranges[144:288])),
            min(max_distance, min(msg.ranges[288:432])),
            min(max_distance, min(msg.ranges[432:576])),
            min(max_distance, min(msg.ranges[576:720]))
            ]
    rospy.loginfo(regions)


def main():
    rospy.init_node('reading_laser')

    sub = rospy.Subscriber('/m2wr/laser/scan', LaserScan, clbk_laser)

    rospy.spin()

if __name__ == '__main__':
    main()
