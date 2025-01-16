# Fuzzy Logic and PID Control for TurtleBot

## Overview
This project showcases a TurtleBot control system using fuzzy logic and PID controllers for autonomous navigation. The robot performs tasks such as right-edge following, obstacle avoidance, and combining behaviors to navigate efficiently and smoothly in dynamic environments.

## Features
- **Fuzzy Logic System:** Processes sensor data with membership functions and rules to make real-time decisions.
- **PID Controller:** Provides precise control for path-following.
- **Obstacle Avoidance:** Utilizes front sensors to detect and avoid obstacles.
- **Right Edge Following:** Maintains a safe distance from the edge using side sensors.
- **Adaptive Logic:** Combines edge-following and obstacle avoidance based on sensor inputs.

## Sensors
- **Right Sensors (RFS, RBS):** Detect distances for edge-following.
- **Front Sensors (F, FR, FL):** Monitor obstacles for collision prevention.

## How It Works
1. **Sensor Inputs:** Data from sensors is processed to evaluate proximity.
2. **Fuzzy Membership Functions:** Map sensor values to defined categories.
3. **Rules and Logic:** Fuzzy rules determine the robot's behavior (e.g., speed and direction adjustments).
4. **Defuzzification:** Converts fuzzy results into actionable outputs for robot movement.
5. **Conditional Logic:** Determines whether to follow the edge or avoid obstacles.

The robot’s linear velocity is fixed at 0.1, while angular velocity is adjusted dynamically based on fuzzy outputs or PID calculations.

## Video Demonstrations
- [PID Control](https://youtube.com/shorts/en-QWag6A8M?feature=share)
- [Right Edge Following](https://youtube.com/shorts/RiOUFpySFm4?feature=share)
- [Obstacle Avoidance](https://youtube.com/shorts/7xEmcVDUwX8?feature=share)
- [Combined Behavior](https://youtube.com/shorts/JMyCX0FFmk8?feature=share)

## Conclusion
This project demonstrates the power of fuzzy logic and PID controllers in robotics. Explore the repository to learn about the implementation and watch the videos to see the TurtleBot in action.
