#!/usr/bin/env python





def main():
    




if __name__ == '__main__':
    
    rospy.init_node('path')
    p = rospy.Publisher('joint_states',JointState, queue_size = 10)
    
    main()
