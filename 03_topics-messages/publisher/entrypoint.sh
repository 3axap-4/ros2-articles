#! /bin/bash
set -e

source /opt/ros/jazzy/setup.bash
source "/app/test_package/install/setup.bash"
ros2 run test_package test_pub_node

exec "$@"