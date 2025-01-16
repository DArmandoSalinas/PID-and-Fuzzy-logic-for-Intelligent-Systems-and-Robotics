import rclpy
import math
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, ReliabilityPolicy
import FuzzyAvoidFront as Fuzzy # Importing the Fuzzy to avoid obstacles
import FuzzySecondSession as FuzzyClass # Importing the Fuzzy to follow the right edge

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


# Main function attached to timer callback
def timer_callback():
    global pub_, twstmsg_
    if twstmsg_ is not None:
        pub_.publish(twstmsg_)


def clbk_laser(msg):
    global regions_, twstmsg_
    regions_ = { # Ranges updated since realizing these ones work better 
        'front1': find_nearest(msg.ranges[0:6]), 
        'front2': find_nearest(msg.ranges[350:360]),
        'right': find_nearest(msg.ranges[260:280]),
        'fright': find_nearest(msg.ranges[300:320]),
        'bright': find_nearest(msg.ranges[210:230]),
        'fleft': find_nearest(msg.ranges[20:40]),
        'left': find_nearest(msg.ranges[70:90]),
        'backwards': find_nearest(msg.ranges[175:185]),
    }

    
    global FRS, FLS, F, RFS, RBS
 

    # Getting movement decision based on the fuzzy logics
    twstmsg_ = movement()


# Find the nearest non-zero point in a list of LIDAR ranges
def find_nearest(lst):
    valid_distances = list(filter(lambda x: x > 0.0, lst))  # exclude zeros
    return min(min(valid_distances, default=1), 1)


# Function to calculate movement based on fuzzy logics
def movement():
    global regions_, RBS, RFS, F, FRS, FLS, BnearFRS, BmediumFRS, BfarFRS, BnearFLS, BmediumFLS, BfarFLS, near, medium, far, low, med, high, left, straight, right, nearF, mediumF, farF
    
    # Creating this variables for the sensor measures in the specific ranges 

    FRS = regions_['fright']  
    FLS = regions_['fleft']  
    F = min(regions_['front1'], regions_['front2'])
    RFS = regions_['fright']  
    RBS = regions_['bright'] 

    # Conditional created to tell the robot how to perform

    # The prefence is going to be following the right edge. But, If there is anything close to the robot from the front right sensor, front left sensor and front. It should perform in order to avoid the obstacles
    if min(FRS, F, FLS) <= 0.45: 

        # Specific lists for this fuzzy logic
        near = [0.0, 0.25, 0.6]
        medium = [0.25, 0.6, 0.7]
        far = [0.6, 0.7, 1.0]

        nearF = [0.0, 0.25, 0.75]
        mediumF = [0.25, 0.75, 0.85]
        farF = [0.75, 0.85, 1.0]

        low = [0.01, 0.05, 0.1]
        med = [0.1, 0.15, 0.2]
        high = [0.2, 0.25, 0.3]

        left = [-0.3, -0.2, -0.1]
        straight = [-0.1, 0.0, 0.1]
        right = [0.1, 0.2, 0.3]

        # Robot's  booleans variables
        BnearFRS = False
        BmediumFRS = False
        BfarFRS = False
        BnearFLS = False
        BmediumFLS = False
        BfarFLS = False
        BnearF = False
        BmediumF = False
        BfarF = False


        msg = Twist()
        print("front right distance", FRS)
        print("front left distance", FLS)
        print("front distance", F)
    
        # Initialize the Fuzzy class

        corre = Fuzzy.FuzzyAvoidFront(FRS = FRS, FLS = FLS, F = F, near=near, medium=medium, far=far, 
                                nearF=nearF, mediumF=mediumF, farF=farF, low=low, med=med, high=high, 
                                left=left, straight=straight, right=right, BnearFRS=BnearFRS, BmediumFRS=BmediumFRS, BfarFRS=BfarFRS, BnearFLS=BnearFLS, 
                                BmediumFLS=BmediumFLS, BfarFLS=BfarFLS, BnearF=BnearF, BmediumF=BmediumF, BfarF=BfarF)

         
        corre.run()  # Perform fuzzy logic operations

        #  Getting the defuzzied ouputs of speed and direction
        speed_output = corre.speed_output 
        direction_output = corre.direction_output 

        # Dictating the speed and direction for the turtlebot
        msg.linear.x = speed_output  
        msg.angular.z = direction_output

        return msg
    
    else: # If there is no obstacles, the robot must perform to follow the wall receiving the inputs of the sensor reading the right side

        # Specific lists for this fuzzy logic

        near = [0, 0.60, 0.65]
        medium = [0.65, 0.7, 0.75]
        far = [0.65, 0.7, 1.0]
        low = [0.01, 0.05, 0.1]
        med = [0.1, 0.15, 0.2]
        high = [0.2, 0.25, 0.3]
        left = [-0.3, -0.2, -0.1]
        straight = [-0.1, 0.0, 0.1]
        right = [0.1, 0.2, 0.3]

        # Boolean variables to the rules

        BnearRFS = False
        BmediumRFS = False
        BfarRFS = False
        BnearRBS = False
        BmediumRBS = False
        BfarRBS = False

        # Initialize the Fuzzy class

        corre = FuzzyClass.Fuzzy(RFS=RFS, RBS=RBS, near=near, medium=medium, far=far,
                              low=low, med=med, high=high, left=left, straight=straight, right=right,
                              BnearRFS=BnearRFS, BmediumRFS=BmediumRFS, BfarRFS=BfarRFS,
                              BnearRBS=BnearRBS, BmediumRBS=BmediumRBS, BfarRBS=BfarRBS)

        corre.run()  # Perform fuzzy logic operations
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
