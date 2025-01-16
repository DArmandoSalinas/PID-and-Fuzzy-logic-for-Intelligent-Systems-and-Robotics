import rclpy
import math
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, ReliabilityPolicy
import FuzzySecondSession as FuzzyClass # I call the class I created  for the right edge

mynode_ = None
pub_ = None
regions_ = {
    'right': 0,
    'fright': 0,
    'bright': 0,
    'front1': 0,
    'front2': 0,
    'fleft': 0,
    'left': 0,
    'backwards': 0,
    'backwards2': 0,
}

twstmsg_ = None

# List and variables for fuzzy logic
near = [0, 0.60, 0.65]
medium = [0.65, 0.7, 0.75]
far = [0.65, 0.7, 1.0]
low = [0.01, 0.05, 0.1]
med = [0.1, 0.15, 0.2]
high = [0.2, 0.25, 0.3]
left = [-0.3, -0.2, -0.1]
straight = [-0.1, 0.0, 0.1]
right = [0.1, 0.2, 0.3]

# Booleans variables for the rules
BnearRFS = False
BmediumRFS = False
BfarRFS = False
BnearRBS = False
BmediumRBS = False
BfarRBS = False


# Main function attached to timer callback
def timer_callback():
    global pub_, twstmsg_
    if twstmsg_ is not None:
        pub_.publish(twstmsg_)


def clbk_laser(msg):
    global regions_, twstmsg_
    regions_ = {
        'front1': find_nearest(msg.ranges[0:5]),
        'front2': find_nearest(msg.ranges[355:360]),
        'right': find_nearest(msg.ranges[265:275]),
        'fright': find_nearest(msg.ranges[310:320]),
        'bright': find_nearest(msg.ranges[215:245]),
        'fleft': find_nearest(msg.ranges[40:50]),
        'left': find_nearest(msg.ranges[85:95]),
        'backwards': find_nearest(msg.ranges[175:185]),
    }

    
    global RFS, RBS
    RFS = regions_['fright']  
    RBS = regions_['bright']  

    # Getting movement decision based on fuzzy logic
    twstmsg_ = movement()


# Find the nearest non-zero point in a list of LIDAR ranges 
def find_nearest(lst):
    valid_distances = list(filter(lambda x: x > 0.0, lst))  # exclude zeros
    return min(min(valid_distances, default=1), 1)


# Function to calculate movement based on fuzzy logic
def movement():
    global regions_, RFS, RBS, BnearRFS, BmediumRFS, BfarRFS, BnearRBS, BmediumRBS, BfarRBS, near, medium, far, low, med, high, left, straight, right 


    # Initialize the Fuzzy class
    corre = FuzzyClass.Fuzzy(RFS=RFS, RBS=RBS, near=near, medium=medium, far=far,
                              low=low, med=med, high=high, left=left, straight=straight, right=right,
                              BnearRFS=BnearRFS, BmediumRFS=BmediumRFS, BfarRFS=BfarRFS,
                              BnearRBS=BnearRBS, BmediumRBS=BmediumRBS, BfarRBS=BfarRBS)

    corre.run()  # To perform fuzzy logic operations by calling the functions
    print(RFS)
    print(RBS)
    msg = Twist()
    print("right distance", regions_['right'])
    print("back right distance", regions_['bright'])

    # Getting the defuzzied ouputs of speed and direction
    speed_output = corre.speed_output 
    direction_output = corre.direction_output 

    # Dictating the speed and direction for the turtlebot
    msg.linear.x = speed_output  
    msg.angular.z = direction_output

    return msg


# Function to stop the robot
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

    # Define QoS profile for subscription
    qos = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)

    # Publisher for sending velocity commands
    pub_ = mynode_.create_publisher(Twist, '/cmd_vel', 10)

    # Subscribe to the laser scan topic
    sub = mynode_.create_subscription(LaserScan, '/scan', clbk_laser, qos)

    # Configure timer to periodically call the timer_callback function
    timer_period = 0.1  # seconds
    timer = mynode_.create_timer(timer_period, timer_callback)

    try:
        rclpy.spin(mynode_)
    except KeyboardInterrupt:
        stop()  # Stop the robot on Ctrl-C
    except Exception as e:
        stop()  # Stop the robot on any other exception
    finally:
        # Clean up
        mynode_.destroy_timer(timer)
        mynode_.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
