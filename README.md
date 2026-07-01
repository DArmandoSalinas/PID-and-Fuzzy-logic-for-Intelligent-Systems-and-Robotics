# Fuzzy Logic & PID Control for TurtleBot

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![ROS](https://img.shields.io/badge/ROS-TurtleBot-22314E.svg)](https://www.ros.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Autonomous **TurtleBot** navigation using **fuzzy logic** and **PID controllers** — right-edge following, obstacle avoidance, and adaptive behavior switching from sensor inputs.

**Author:** [Diego Armando Salinas Lugo](https://sites.google.com/tec.mx/salinasdiegoarmando/know-me)

---

## Features

- Fuzzy membership functions and rule-based decision making
- PID controller for precise path following
- Front sensors (F, FR, FL) for obstacle avoidance
- Side sensors (RFS, RBS) for edge following
- Combined adaptive logic for dynamic environments

## How it works

1. Read proximity from TurtleBot sensors
2. Map values to fuzzy categories via membership functions
3. Apply fuzzy rules → defuzzify to velocity commands
4. Switch between edge-following and avoidance modes

Linear velocity fixed at **0.1**; angular velocity adjusted dynamically.

## Prerequisites

- ROS-compatible TurtleBot environment
- Python 3.x with project dependencies
- Sensor drivers configured for your robot platform

## Demo videos

| Behavior | Link |
|----------|------|
| PID control | [Watch](https://youtube.com/shorts/en-QWag6A8M) |
| Right edge following | [Watch](https://youtube.com/shorts/RiOUFpySFm4) |
| Obstacle avoidance | [Watch](https://youtube.com/shorts/7xEmcVDUwX8) |
| Combined behavior | [Watch](https://youtube.com/shorts/JMyCX0FFmk8) |

## License

MIT — see [LICENSE](LICENSE).
