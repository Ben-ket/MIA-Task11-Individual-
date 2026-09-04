#!/bin/bash
killall -9 gz sim ruby 2>/dev/null
colcon build --symlink-install
source install/setup.bash
ros2 launch vehicle_sim sim.launch.py
