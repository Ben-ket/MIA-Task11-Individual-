# 4-Wheel Robot Simulation (ROS 2 Jazzy)

A simple ROS 2 Jazzy and Gazebo Harmonic package for simulating a 4-wheeled differential drive robot equipped with a camera sensor.

## Features

* **URDF / XACRO Model**: Blue chassis, 4 black wheels built using XACRO macros, and a red front camera.
* **Differential Drive**: Controlled via `gz-sim-diff-drive-system` plugin.
* **Camera Stream**: Simulates a vision sensor publishing camera frames.
* **ROS 2 Bridge**: Shares `/cmd_vel` and `/camera/image_raw` topics between ROS 2 and Gazebo.

## Requirements

* ROS 2 Jazzy
* Gazebo Harmonic (`ros_gz`)
* `robot_state_publisher`, `joint_state_publisher_gui`, `rviz2`

## How to Run

1. Clone or copy this repository into your ROS 2 workspace `src` folder (e.g., `ros2_ws/src/vehicle_sim`).
2. Make sure the run script is executable and start the simulation:

```bash
chmod +x run.sh
./run.sh

```

This script cleans background processes, builds the package with `colcon`, sources the environment, and starts Gazebo and RViz together.

## Moving the Robot

Open a new terminal, source your ROS 2 installation, and publish velocity commands to drive the vehicle:

```bash
source /opt/ros/jazzy/setup.bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.2}}"

```

## Main Topics

* `/cmd_vel` (`geometry_msgs/msg/Twist`): Controls linear and angular velocity.
* `/camera/image_raw` (`sensor_msgs/msg/Image`): Live camera video feed.
* `/joint_states` (`sensor_msgs/msg/JointState`): Wheel joint positions.
