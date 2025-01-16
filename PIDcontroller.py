import rclpy
import math

from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf2_ros import TransformRegistration
from rclpy.qos import QoSProfile, ReliabilityPolicy


mynode_ = None
pub_ = None
regions_ = {
    'right': 0,
    'fright': 0,
    'front1': 0,
    'front2': 0,
    'fleft': 0,
    'left': 0,
    'backwards': 0,
    'backwards2': 0,
}

twstmsg_ = None

#After trying with so many parameters these were the ones that worked better for me, CSEETURTLEBOT21 or CSEETURTLEBOT04
Kp = 0.3 
Ki = 0.0001
Kd = 0.0

#Initializing the variables
eprev = 0
e = 0
ei = 0 
ed = 0 

#The distance desired to take decisions
DesDis = 0.25
CurrentDis = regions_['right']


# main function attached to timer callback
def timer_callback():
    global pub_, twstmsg_
    if ( twstmsg_ != None ):
        pub_.publish(twstmsg_)


def clbk_laser(msg):
    global regions_, twstmsg_
    regions_ = { 
        #LIDAR readings are anti-clockwise
        'front1':  find_nearest (msg.ranges[0:5]),
        'front2':  find_nearest (msg.ranges[355:360]),
        'right':  find_nearest(msg.ranges[265:275]),
        'fright': find_nearest (msg.ranges[310:320]),
        'fleft':  find_nearest (msg.ranges[40:50]),
        'left':   find_nearest (msg.ranges[85:95]),
        'backwards': find_nearest(msg.ranges[175:185]),
    }    
    twstmsg_= movement()

    
# Find nearest point
def find_nearest(list):
    f_list = filter(lambda item: item > 0.0, list)  # exclude zeros
    return min(min(f_list, default=10), 10)

#Movement function in which I import the control constants, the formulas to update the variables that affect the final output which will determine the angular velocity. 
def movement():

    global regions_, mynode_, eprev, ei, Kp, Ki, Kd
    regions = regions_

    CurrentDis = regions_['right'] # Measures the distance at the right side
    e = DesDis - CurrentDis # check the error
    ei += e # The integral error
    ed = e - eprev # The derivative error
    eprev = e # The prevoius error
      
    output = Kp * e + Ki * ei + Kd * ed # Formula to get the output. In this case the Kd*ed are 0 since i let 0 as the Kd because the as the speed of the robot is too slow, this parameter is no needed.

    
    print("Distance in front region: ", regions_['front1'],regions_['front2'])
    print("Distance in right region: ", regions_['right'])
    print("output", output)

    #create an object of twist class, used to express the linear and angular velocity of the turtlebot 
    msg = Twist()

    msg.linear.x = 0.1 # Constant velocity
    msg.angular.z =  output # Angular speed will depend in the PID control formula which depends in the constants and the updated errors.
    

    
    # I created this conditionals for specific scenarios to avoid the robot to crash

    # I created this conditions just for the robot not crash at the moment it turns, since there are points in which the front right sensor can sense the wall and the right one no
    if regions_['fright'] <= 0.25:
        msg.linear.x = 0.1
        msg.angular.z =  0.40 #With this values the robot will turn to the left to correct its path

    # This conditionals is for the robot not crash if it is going straight to something.
    if regions_['front1'] <= 0.35 or regions_['front2'] <= 0.35:
        msg.linear.x = 0.1
        msg.angular.z =  0.8 #With this values the robot will turn to the left to correct its path, its a higher value since more action is needed

    return msg


#used to stop the rosbot
def stop():
    global pub_
    msg = Twist()
    msg.angular.z = 0.0
    msg.linear.x = 0.0
    pub_.publish(msg)  
    

def main():
    global pub_, mynode_

    rclpy.init()
    mynode_ = rclpy.create_node('reading_laser')

    # define qos profile (the subscriber default 'reliability' is not compatible with robot publisher 'best effort')
    qos = QoSProfile(
        depth=10,
        reliability=ReliabilityPolicy.BEST_EFFORT,
    )

    # publisher for twist velocity messages (default qos depth 10)ar.x 
    pub_ = mynode_.create_publisher(Twist, '/cmd_vel', 10)

    # subscribe to laser topic (with our qos)
    sub = mynode_.create_subscription(LaserScan, '/scan', clbk_laser, qos)

    # Configure timer
    timer_period = 0.2  # seconds 
    timer = mynode_.create_timer(timer_period, timer_callback)

    # Run and handle keyboard interrupt (ctrl-c)
    try:
        rclpy.spin(mynode_)
    except KeyboardInterrupt:
        stop()  # stop the robot
    except:
        stop()  # stop the robot
    finally:
        # Clean up
        mynode_.destroy_timer(timer)
        mynode_.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
